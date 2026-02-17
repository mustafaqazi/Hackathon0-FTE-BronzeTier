#!/usr/bin/env python3
"""
AI Employee Orchestrator - Bronze Tier
Central coordination system for task management and automation
"""

import os
import sys
from pathlib import Path
from datetime import datetime
from watchers.filesystem_watcher import FilesystemWatcher

class Orchestrator:
    """Main orchestration system for Bronze Tier"""

    def __init__(self):
        """Initialize the orchestrator"""
        self.base_path = Path(__file__).parent
        self.vault_path = self.base_path / 'vault'
        self.watcher = FilesystemWatcher(self.vault_path)
        self.start_time = datetime.now()

    def initialize(self):
        """Initialize the orchestrator system"""
        print("[AI] AI Employee Orchestrator - Bronze Tier")
        print("=" * 50)
        print(f"Base Path: {self.base_path}")
        print(f"Vault Path: {self.vault_path}")
        print(f"Started at: {self.start_time.isoformat()}\n")

        if not self.watcher.initialize():
            print("[!] Failed to initialize filesystem watcher")
            return False

        print("[OK] Orchestrator initialized successfully\n")
        return True

    def check_system_status(self):
        """Check overall system status"""
        print("[*] System Status Check")
        print("-" * 50)

        # Check directories
        vault_status = self.watcher.check_vault_status()

        print(f"Vault Status: {'[OK] Online' if vault_status['vault_exists'] else '[!] Offline'}")
        print(f"Timestamp: {vault_status['timestamp']}\n")

        print("Directory Status:")
        for dir_name, info in vault_status['directories'].items():
            status = "[OK]" if info['exists'] else "[!]"
            print(f"  {status} {dir_name}: {info['file_count']} items")

        return vault_status['vault_exists']

    def show_dashboard(self):
        """Display orchestrator dashboard"""
        print("\n[DASHBOARD] AI Employee Dashboard")
        print("=" * 50)

        # Check vault files
        inbox = self.vault_path / 'Inbox'
        needs_action = self.vault_path / 'Needs_Action'
        done = self.vault_path / 'Done'

        inbox_count = len(list(inbox.glob('*'))) if inbox.exists() else 0
        action_count = len(list(needs_action.glob('*'))) if needs_action.exists() else 0
        done_count = len(list(done.glob('*'))) if done.exists() else 0

        print(f"[INBOX] Inbox:           {inbox_count} items")
        print(f"[ACTION] Needs Action:    {action_count} items")
        print(f"[DONE] Done:            {done_count} items")
        print("=" * 50)

    def run(self):
        """Run the orchestrator"""
        if not self.initialize():
            sys.exit(1)

        self.check_system_status()
        self.show_dashboard()

        print("\n[READY] Bronze Tier Orchestrator Ready")
        print("Type 'help' for available commands or 'exit' to quit\n")

def main():
    """Main entry point"""
    orchestrator = Orchestrator()
    orchestrator.run()

if __name__ == '__main__':
    main()
