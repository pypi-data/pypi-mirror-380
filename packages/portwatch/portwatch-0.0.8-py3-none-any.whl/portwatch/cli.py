import asyncio
import psutil
from typing import List, Dict, Any, Optional
from concurrent.futures import ThreadPoolExecutor
import threading
import time

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, DataTable, Input, Static, Button
from textual.screen import ModalScreen
from textual.containers import Horizontal, Container, Vertical
from textual import on
from textual.events import Key

from .scaner import scan_ports, scan_changes, check_for_conflict
from pathlib import Path
import yaml
from .notifyer import alert_conflict,alert_process_killed,alert_conflict_sync 

# Global thread pool for CPU-intensive tasks
THREAD_POOL = ThreadPoolExecutor(max_workers=2)

class DataCache:
    """Thread-safe data cache with efficient updates"""
    def __init__(self):
        self._lock = threading.RLock()
        self._raw_data: List[Dict[str, Any]] = []
        self._previous_data: List[Dict[str, Any]] = []
        self._last_scan_time = 0
        self._processed_cache = {}  # Cache for processed table data
        
    def update_raw_data(self, new_data: List[Dict[str, Any]]) -> bool:
        """Update raw data and return True if data actually changed"""
        with self._lock:
            # Quick comparison to avoid unnecessary updates
            if len(new_data) == len(self._raw_data):
                # Deep comparison only if lengths match
                if self._data_equal(new_data, self._raw_data):
                    return False
            
            self._previous_data = self._raw_data.copy()
            self._raw_data = new_data.copy()
            self._last_scan_time = time.time()
            # Clear processed cache when raw data changes
            self._processed_cache.clear()
            return True
    
    def get_data(self) -> tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        """Get current and previous data"""
        with self._lock:
            return self._raw_data.copy(), self._previous_data.copy()
    
    def get_processed_data(self, cache_key: str) -> Optional[List[tuple]]:
        """Get cached processed data"""
        with self._lock:
            return self._processed_cache.get(cache_key)
    
    def set_processed_data(self, cache_key: str, data: List[tuple]) -> None:
        """Cache processed data"""
        with self._lock:
            self._processed_cache[cache_key] = data
    
    def _data_equal(self, data1: List[Dict], data2: List[Dict]) -> bool:
        """Fast comparison of data lists"""
        if len(data1) != len(data2):
            return False
        
        # Create sets of key identifiers for quick comparison
        set1 = {(d.get('pid'), d.get('port'), d.get('process_name')) for d in data1}
        set2 = {(d.get('pid'), d.get('port'), d.get('process_name')) for d in data2}
        
        return set1 == set2


async def map_table_optimized(data_list: List[Dict[str, Any]], old_data: List[Dict[str, Any]], 
                             filter_mode: str, cache: DataCache) -> List[tuple]:
    """Optimized table mapping with caching"""
    
    # Create cache key
    data_hash = hash(str(sorted([(d.get('pid'), d.get('port')) for d in data_list])))
    cache_key = f"{filter_mode}_{data_hash}"
    
    # Try to get from cache first
    cached_result = cache.get_processed_data(cache_key)
    if cached_result is not None:
        return cached_result
    
    # Process in thread pool to avoid blocking UI
    loop = asyncio.get_event_loop()
    
    def process_data():
        from .utils import get_port_description
        
        table_data = []
        # Pre-compute changes once
        changes = []
        try:
            # Run scan_changes in thread since it might be CPU intensive
            loop_for_thread = asyncio.new_event_loop()
            asyncio.set_event_loop(loop_for_thread)
            changes = loop_for_thread.run_until_complete(scan_changes(old_data, data_list))
            loop_for_thread.close()
        except Exception as e:
            print(f"Error in scan_changes: {e}")
            changes = []
        
        changes_set = set(id(item) for item in changes) if changes else set()
        
        for item in data_list:
            pid = str(item.get("pid", "")) if item.get("pid") is not None else ""
            port = str(item.get("port", ""))
            process_name = item.get("process_name", "") or ""
            status = item.get("status", "") or ""
            action_label = "[red]KILL[/red]"
            
            note_parts = []
            
            # Use pre-computed flags
            is_new = id(item) in changes_set
            is_conflict = bool(item.get("note"))
            
            # Send conflict alerts (do this sparingly)
            if is_conflict:
                try:
                    alert_conflict(port, app_name=process_name)
                except Exception:
                    pass  # Don't let notification errors break the app
            
            # Apply filter mode
            if filter_mode == "conflict" and not is_conflict:
                continue
            elif filter_mode == "new" and not is_new:
                continue
            
            # Build notes
            if filter_mode == "all":
                if is_new:
                    note_parts.append("[green]NEW[/green]")
                if is_conflict:
                    note_parts.append("[yellow]⚠ Conflict[/yellow]")
            elif filter_mode == "conflict":
                note_parts.append("[yellow]⚠ Conflict[/yellow]")
            elif filter_mode == "new":
                note_parts.append("[green]NEW[/green]")
            
            note = " ".join(note_parts)
            table_data.append((pid, port, process_name, status, action_label, note))

            if is_new and is_conflict:
                # Send conflict alerts (do this sparingly)
                try:
                    alert_conflict_sync(port, app_name=process_name)
                except Exception:
                    pass  # Don't let notification errors break the app
        return table_data
    
    # Run processing in thread pool
    result = await loop.run_in_executor(THREAD_POOL, process_data)
    
    # Cache the result
    cache.set_processed_data(cache_key, result)
    
    return result


def apply_text_filter_optimized(data_list: List[Dict[str, Any]], text_filter: Optional[str]) -> List[Dict[str, Any]]:
    """Optimized text filtering with early returns"""
    if not text_filter:
        return data_list
    
    text_filter = text_filter.lower()
    filtered_data = []
    
    for item in data_list:
        # Quick string checks without unnecessary conversions
        pid_str = str(item.get("pid", ""))
        port_str = str(item.get("port", ""))
        process_str = item.get("process_name", "") or ""
        
        # Use 'in' operator directly on strings (case-insensitive)
        if (text_filter in pid_str.lower() or 
            text_filter in port_str.lower() or 
            text_filter in process_str.lower()):
            filtered_data.append(item)
    
    return filtered_data


class KillConfirmation(ModalScreen[bool]):
    def __init__(self, pid: int, process_name: str) -> None:
        super().__init__()
        self.pid = pid
        self.process_name = process_name

    def compose(self) -> ComposeResult:
        yield Container(
            Static(
                f"Do you really want to KILL\n\n[bold red]{self.process_name}[/] (PID {self.pid})?",
                classes="dialog-message",
            ),
            Horizontal(
                Button("Yes", id="yes"),
                Button("No", id="no"),
                classes="dialog-buttons",
            ),
            classes="dialog-box",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "yes":
            # Run kill operation in thread pool
            async def kill_process():
                loop = asyncio.get_event_loop()
                
                def do_kill():
                    try:
                        proc = psutil.Process(self.pid)
                        proc.terminate()
                        gone, alive = psutil.wait_procs([proc], timeout=3)
                        if proc in gone:
                            return True
                        else:
                            proc.kill()
                            gone, alive = psutil.wait_procs([proc], timeout=2)
                            return True
                    except psutil.NoSuchProcess:
                        return True  # already gone
                    except Exception:
                        return False
                
                result = await loop.run_in_executor(THREAD_POOL, do_kill)
                self.dismiss(result)
            
            asyncio.create_task(kill_process())
            
        elif event.button.id == "no":
            self.dismiss(False)


class PortWatch(App):
    CSS = """
    Screen {
        background: $surface;
    }

    Header {
        background: $primary;
        color: $text;
        text-style: bold;
    }

    #main_content {
        padding: 1 2;
        height: 100%;
    }

    #filter_bar {
        height: auto;
        padding: 1 0;
        align: center middle;
        background: $background;
        border: tall $primary 20%;
        margin-bottom: 1;
    }

    #filter_bar .icon {
        color: $text-disabled;
        width: 4;
        content-align: center middle;
    }

    .filter_input {
        width: 50%;
        margin-right: 1;
    }

    .filter_btn {
        width: auto;
        min-width: 10;
        padding: 0 2;
        border: none;
        color: $text;
        background: transparent;
        transition: background 0.2s;
    }

    .filter_btn:hover {
        background: $primary 20%;
    }

    .filter_btn--active {
        background: $secondary;
        color: $text;
        border: tall $secondary;
    }

    .config_btn {
        margin-left: 2;
        padding: 0 2;
        height: 3;
    }

    .data_table {
        height: 1fr;
        border: tall $primary 15%;
    }

    .data_table > .datatable--header {
        background: $primary 15%;
        color: $text;
        text-style: bold;
        padding: 0 1;
    }

    .data_table > .datatable--cursor,
    .data_table > .datatable--even,
    .data_table > .datatable--odd {
        padding: 0 1;
    }

    Footer {
        background: $primary;
        color: $text;
    }
"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.filter: Optional[str] = None
        self.filter_mode: str = "all"  # "all", "new", "conflict"
        
        # Use optimized data cache
        self._data_cache = DataCache()
        self._refresh_in_progress = False
        
        # Debounce filtering
        self._filter_task: Optional[asyncio.Task] = None
        self._last_filter_time = 0

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Vertical(id="main_content"):
            with Horizontal(id="filter_bar"):
                yield Static("🔍", classes="icon")
                yield Input(
                    id="input",
                    placeholder="Filter processes or ports (e.g. Chrome, 3000)",
                    classes="filter_input"
                )
                yield Button("All", id="filter_all", classes="filter_btn filter_btn--active")
                yield Button("🆕 New", id="filter_new", classes="filter_btn")
                yield Button("⚠️ Conflict", id="filter_conflict", classes="filter_btn")
                yield Button("⚙️ Config", id="open_config", variant="primary", classes="config_btn")
            yield DataTable(id="port_table", classes="data_table")
        yield Footer()

    # Optimized filter button handlers
    @on(Button.Pressed, "#filter_all")
    def set_filter_all(self):
        if self.filter_mode != "all":
            self.filter_mode = "all"
            self.update_button_styles()
            self._schedule_instant_refresh()

    @on(Button.Pressed, "#filter_new")
    def set_filter_new(self):
        if self.filter_mode != "new":
            self.filter_mode = "new"
            self.update_button_styles()
            self._schedule_instant_refresh()

    @on(Button.Pressed, "#filter_conflict")
    def set_filter_conflict(self):
        if self.filter_mode != "conflict":
            self.filter_mode = "conflict"
            self.update_button_styles()
            self._schedule_instant_refresh()

    def update_button_styles(self):
        """Highlight active filter button."""
        for mode in ["all", "new", "conflict"]:
            button = self.query_one(f"#filter_{mode}", Button)
            if self.filter_mode == mode:
                button.add_class("filter_btn--active")
            else:
                button.remove_class("filter_btn--active")

    @on(Button.Pressed, "#open_config")
    async def open_config_modal(self):
        from .portconfig_screen import PortConfigModal
        await self.push_screen(PortConfigModal())

    @on(Input.Changed)
    def input_changed(self, event: Input.Changed) -> None:
        new_filter = event.value.strip() or None
        if new_filter != self.filter:
            self.filter = new_filter
            self._schedule_debounced_filter()

    def _schedule_instant_refresh(self):
        """Schedule instant refresh without debouncing"""
        if self._filter_task and not self._filter_task.done():
            self._filter_task.cancel()
        self._filter_task = asyncio.create_task(self._refresh_display_instantly())

    def _schedule_debounced_filter(self):
        """Schedule debounced filter update"""
        self._last_filter_time = time.time()
        
        if self._filter_task and not self._filter_task.done():
            self._filter_task.cancel()
        
        # Debounce text input by 150ms
        async def debounced_update():
            await asyncio.sleep(0.15)
            if time.time() - self._last_filter_time >= 0.14:  # Only update if no recent changes
                await self._refresh_display_instantly()
        
        self._filter_task = asyncio.create_task(debounced_update())

    async def on_ready(self) -> None:
        self.table = self.query_one("#port_table", DataTable)
        self.table.cursor_type = "row"

        if not self.table.columns:
            self.table.add_columns("PID", "PORT", "PROCESS", "STATUS", "ACTION", "NOTE")

        # Initial scan and start background refresh
        await self._do_data_scan()
        asyncio.create_task(self._background_refresh_loop())

    async def _background_refresh_loop(self) -> None:
        """Optimized background loop"""
        while True:
            await asyncio.sleep(2)  # Check every 2 seconds
            if not self._refresh_in_progress:
                # Only scan if we haven't scanned recently
                if time.time() - self._data_cache._last_scan_time > 1.5:
                    await self._do_data_scan()

    async def _do_data_scan(self) -> None:
        """Optimized data scanning"""
        if self._refresh_in_progress:
            return
            
        try:
            self._refresh_in_progress = True
            
            # Run scan in thread pool
            loop = asyncio.get_event_loop()
            new_conns = await loop.run_in_executor(THREAD_POOL, lambda: asyncio.run(scan_ports(None)))
            
            # Only update if data actually changed
            if self._data_cache.update_raw_data(new_conns):
                await self._refresh_display_instantly()
                self.log(f"PortWatch: scanned {len(new_conns)} connections")
            
        except Exception as e:
            self.log(f"PortWatch error during scan: {e}")
        finally:
            self._refresh_in_progress = False

    async def _refresh_display_instantly(self) -> None:
        """Instant display refresh using cached data"""
        try:
            current_data, old_data = self._data_cache.get_data()
            if not current_data:
                return
            
            # Apply text filter in thread pool
            loop = asyncio.get_event_loop()
            filtered_data = await loop.run_in_executor(
                THREAD_POOL, 
                apply_text_filter_optimized, 
                current_data, 
                self.filter
            )
            
            # Generate table rows with caching
            rows = await map_table_optimized(filtered_data, old_data, self.filter_mode, self._data_cache)
            
            # Update table efficiently
            await self._update_table_efficiently(rows)
            
        except Exception as e:
            self.log(f"PortWatch error during instant refresh: {e}")

    async def _update_table_efficiently(self, rows: List[tuple]) -> None:
        """Efficiently update table with minimal UI disruption"""
        try:
            # Store current scroll and cursor position
            old_scroll_y = getattr(self.table.scroll_offset, 'y', 0) if hasattr(self.table, 'scroll_offset') else 0
            cursor_row = getattr(self.table.cursor_coordinate, 'row', 0) if hasattr(self.table, 'cursor_coordinate') else 0
            
            # Clear table
            self.table.clear()
            
            if rows:
                # Add all rows at once
                self.table.add_rows(rows)
                
                # Restore position after a tiny delay to let UI settle
                if old_scroll_y > 0 or cursor_row > 0:
                    async def restore_position():
                        await asyncio.sleep(0.01)
                        try:
                            if old_scroll_y > 0:
                                self.table.scroll_to(y=old_scroll_y)
                            if cursor_row > 0 and cursor_row < len(rows):
                                self.table.move_cursor(row=cursor_row)
                        except Exception:
                            pass
                    
                    asyncio.create_task(restore_position())

            self.log(f"PortWatch: display updated with {len(rows)} rows")
            
        except Exception as e:
            self.log(f"PortWatch error during table update: {e}")

    @on(DataTable.RowSelected)
    async def handle_row_selected(self, event: DataTable.RowSelected) -> None:
        try:
            row = self.table.get_row(event.row_key)
        except Exception:
            coord = getattr(self.table, "cursor_coordinate", None)
            if coord is None:
                self.notify("No row selected", severity="error")
                return
            row = self.table.get_row(coord.row)

        if not row:
            self.notify("Row data not available", severity="error")
            return

        pid_str = str(row[0]).strip()
        process_name = str(row[2]).strip() if len(row) > 2 else ""

        try:
            pid = int(pid_str)
        except Exception:
            self.notify("Invalid PID", severity="error")
            return

        # Open confirmation modal and wait
        result = await self.push_screen(KillConfirmation(pid, process_name))

        if result is True:
            self.notify(f"Killed PID {pid}", severity="success")
            await self._do_data_scan()  # Force immediate scan after kill
        elif result is False:
            self.notify("Kill cancelled", severity="info")
        else:
            self.notify("No action taken", severity="info")


class NotificationNotEnabledAlert(ModalScreen[None]): 
    CSS = """
    NotificationNotEnabledAlert {
        align: center middle;
    }

    #alert-dialog {
        width: 60%;
        max-width: 500;
        height: auto;
        padding: 2 4;
        border: thick $error 80%;
        background: $surface;
        content-align: center middle;
    }

    #alert-dialog Static {
        text-align: center;
        width: 100%;
        padding: 1 0;
    }

    #alert-dialog Button {
        margin-top: 2;
        width: 50%;
    }
    """

    def compose(self) -> ComposeResult:
        with Vertical(id="alert-dialog"):
            yield Static("🔔 Notifications Disabled", classes="header")
            yield Static(
                "Desktop notifications are not available or not enabled on this system.\n"
                "You may not receive alerts for port conflicts or process kills.",
                classes="message"
            )
            yield Button("OK", variant="primary", id="ok")

    @on(Button.Pressed, "#ok")
    def close_alert(self, event: Button.Pressed) -> None:
        self.dismiss()

    def on_key(self, event: Key) -> None:
        if event.key in ("enter", "escape", "space"):
            self.dismiss()
            event.stop()


def main():
    app = PortWatch()
    try:
        app.run()
    finally:
        # Clean up thread pool
        THREAD_POOL.shutdown(wait=True)


if __name__ == "__main__":
    main()