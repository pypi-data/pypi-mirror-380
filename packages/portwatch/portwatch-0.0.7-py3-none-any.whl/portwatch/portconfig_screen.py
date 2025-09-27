# portconfig_screen.py

from pathlib import Path
import yaml
from typing import List
from textual.screen import ModalScreen
from textual.widgets import Header, Footer, Button, Input, DataTable, Static
from textual.containers import VerticalScroll, Horizontal
from textual.app import ComposeResult
import subprocess
import sys

from .utils import load_dev_ports, save_dev_ports, add_dev_port, remove_dev_port, reset_dev_ports_to_default

CONFIG_FILE = Path(".portconfig")


class PortConfigModal(ModalScreen[None]):
    CSS = """
    PortConfigModal {
        align: center middle;
    }

    #modal-container {
        width: 60%;
        height: 80%;
        border: thick $background 80%;
        padding: 1;
    }

    #ports_table {
        height: 50%;
        width: 100%;
        margin-bottom: 1;
    }

    #input_container {
        layout: horizontal;
        align: center bottom;
        height: auto;
        margin-bottom: 1;
    }

    #input_port {
        width: 70%;
    }

    Button {
        margin-left: 1;
    }
    
    #button_row {
        layout: horizontal;
        align: center bottom;
        height: auto;
    }
    """

    def __init__(self):
        super().__init__()
        self.ports = load_dev_ports()  
        self.table = None
        self.input_box = None

    def compose(self) -> ComposeResult:
        with VerticalScroll(id="modal-container"):
            yield Header(show_clock=False)
            yield Static("⚙️ Manage Dev Ports", id="title")
            self.table = DataTable(id="ports_table")
            yield self.table
            with Horizontal(id="input_container"):
                self.input_box = Input(placeholder="Enter port to add (1-65535)", id="input_port")
                yield self.input_box
                yield Button("Add Port", id="add_port", variant="success")
            with Horizontal(id="button_row"):
                yield Button("Delete Selected", id="delete_port", variant="error")
                yield Button("Reset to Default", id="reset_ports", variant="warning")
                yield Button("Open Config", id="open_config", variant="primary")
            yield Button("Close", id="close", variant="primary")
            yield Footer()

    def on_mount(self):
        self.refresh_table()

    def refresh_table(self):
        self.table.clear()
        self.table.add_columns("Port", "Description")
        for port in self.ports:
            desc = self.get_port_description(port)
            self.table.add_row(str(port), desc)

    def get_port_description(self, port: int) -> str:
        from .utils import get_port_description
        return get_port_description(port)

    def on_button_pressed(self, event: Button.Pressed):
        button_id = event.button.id
        
        if button_id == "add_port":
            port_text = self.input_box.value.strip()
            if port_text.isdigit():
                port = int(port_text)
                if 1 <= port <= 65535:
                    if add_dev_port(port):   
                        self.ports = load_dev_ports()
                        self.refresh_table()
                        self.notify(f"✅ Added port {port}", severity="information")
                    else:
                        self.notify(f"ℹ️ Port {port} already exists", severity="warning")
                else:
                    self.notify("❌ Port must be 1-65535", severity="error")
            else:
                self.notify("❌ Please enter a valid port number", severity="error")
            self.input_box.value = ""
            
        elif button_id == "delete_port":
            if self.table.cursor_row is not None:
                row_index = self.table.cursor_row
                row = self.table.get_row_at(row_index)
                port = int(row[0])
                if remove_dev_port(port):  
                    self.ports = load_dev_ports()
                    self.refresh_table()
                    self.notify(f"🗑️ Removed port {port}", severity="warning")
                else:
                    self.notify(f"⚠️ Port {port} not found", severity="error")
            else:
                self.notify("❌ No port selected", severity="error")
                
        elif button_id == "reset_ports":
            reset_dev_ports_to_default()  
            self.ports = load_dev_ports()
            self.refresh_table()
            self.notify("🔄 Reset to default ports", severity="warning")
            
        elif button_id == "open_config":
            self.open_config_file()
            
        elif button_id == "close":
            self.dismiss()

    def open_config_file(self):
        """Open the config file in the default text editor"""
        try:
            if sys.platform.startswith('darwin'):  # macOS
                subprocess.run(['open', str(CONFIG_FILE)])
            elif sys.platform.startswith('win'):   # Windows
                subprocess.run(['start', str(CONFIG_FILE)], shell=True)
            else:  # Linux and others
                subprocess.run(['xdg-open', str(CONFIG_FILE)])
            self.notify(f"📂 Opened config file: {CONFIG_FILE}", severity="information")
        except Exception as e:
            self.notify(f"❌ Could not open config file: {e}", severity="error")