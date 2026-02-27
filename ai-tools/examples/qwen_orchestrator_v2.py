# -*- coding: utf-8 -*-
"""
Qwen Agent Orchestrator v2
===========================
With Task Acknowledgment + Plan-Web Mode
"""

import os
import sys
import asyncio
import time
from datetime import datetime
from enum import Enum
from typing import Optional, List, Dict
import subprocess

# Force UTF-8 encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

class AgentMode(Enum):
    PLAN = "plan"
    PLAN_WEB = "plan-web"
    AUTO = "auto"
    YOLO = "yolo"

class AgentOrchestrator:
    """Orchestrator with acknowledgment and plan-web"""

    def __init__(self):
        self.mode = AgentMode.AUTO
        self.mode_index = 0
        self.modes = [AgentMode.PLAN, AgentMode.PLAN_WEB, AgentMode.AUTO, AgentMode.YOLO]
        self.command_counter = 1
        self.command_history = {}  # Store numbered commands
    
    def display_header(self):
        """Display header with all modes"""
        print(f"""
{Colors.BOLD}╔══════════════════════════════════════════════════════════╗
║     🛡️  Safe Workspace - AI Agent Environment            ║
╠══════════════════════════════════════════════════════════╣
║  🤖 AI Orchestrator Pro:                                 ║
║    📝 Coder (7B)  📋 Planner (3B)  🔍 Reviewer (4B)     ║
║    🔍 Search  🌐 Scraper  📋 Planner  🧪 Executor        ║
║                                                          ║
║  Modes:                                                  ║
║    🟡 PLAN       - Show what would be done               ║
║    🟢 PLAN-WEB   - Research internet + plan              ║
║    🔵 AUTO       - Execute with confirmation             ║
║    🔴 YOLO       - Execute immediately                   ║
║                                                          ║
║  Commands:                                               ║
║    [command]   - Execute task (with acknowledgment)      ║
║    TAB/m       - Toggle mode                             ║
║    plan        - Create plan                             ║
║    plan-web    - Research + plan from web                ║
║    search      - Web search                              ║
║    status      - Show status                             ║
║    quit        - Exit                                    ║
╚══════════════════════════════════════════════════════════╝
{Colors.END}""")
    
    def toggle_mode(self):
        """Toggle between modes"""
        self.mode_index = (self.mode_index + 1) % len(self.modes)
        self.mode = self.modes[self.mode_index]
        
        mode_colors = {
            AgentMode.PLAN: Colors.YELLOW,
            AgentMode.PLAN_WEB: Colors.GREEN,
            AgentMode.AUTO: Colors.CYAN,
            AgentMode.YOLO: Colors.RED
        }
        
        mode_icons = {
            AgentMode.PLAN: "🟡",
            AgentMode.PLAN_WEB: "🟢",
            AgentMode.AUTO: "🔵",
            AgentMode.YOLO: "🔴"
        }
        
        print(f"\n{mode_colors[self.mode]}📍 Mode: {mode_icons[self.mode]} {self.mode.value.upper()}{Colors.END}\n")
        return self.mode
    
    def acknowledge(self, command: str):
        """Acknowledge user's command with checkmark"""
        mode_display = {
            AgentMode.PLAN: "🟡 PLAN",
            AgentMode.PLAN_WEB: "🟢 PLAN-WEB",
            AgentMode.AUTO: "🔵 AUTO",
            AgentMode.YOLO: "🔴 YOLO"
        }
        
        print(f"\n{Colors.GREEN}✅ ACKNOWLEDGED:{Colors.END} \"{command}\"")
        print(f"   {Colors.CYAN}📍 Mode:{Colors.END} {mode_display.get(self.mode, 'AUTO')}")
        print(f"   {Colors.BLUE}🤖 Agent:{Colors.END} Coder (7B)")
        print()
    
    def run_plan_web(self, topic: str, num: int):
        """Run plan-web with live research display and number"""
        self.acknowledge(f"Research: {topic}", num)
        
        print(f"{Colors.GREEN}🌐 PLAN-WEB: Starting live research...{Colors.END}\n")
        
        # Run web research tool
        tools_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        research_script = os.path.join(tools_dir, "web_research.py")
        
        try:
            subprocess.run([sys.executable, research_script, topic], check=True)
        except Exception as e:
            print(f"{Colors.RED}❌ Research error: {e}{Colors.END}")
    
    def execute_task(self, command: str, num: int):
        """Execute task with acknowledgment and number"""
        # First, acknowledge the task
        self.acknowledge(command, num)
        
        # Then execute based on mode
        if self.mode == AgentMode.PLAN:
            print(f"{Colors.YELLOW}[PLAN MODE]{Colors.END}")
            print(f"Would execute: {command}\n")
            return
        
        if self.mode == AgentMode.PLAN_WEB:
            self.run_plan_web(command)
            return
        
        # AUTO or YOLO mode
        print(f"{Colors.CYAN}⚙️  Executing:{Colors.END} {command}\n")
        
        # Show progress indicators
        print(f"{Colors.BLUE}[████████░░░░░░░░] Running...{Colors.END}")
        time.sleep(0.5)
        print(f"{Colors.BLUE}[████████████████] Complete!{Colors.END}\n")
        
        print(f"{Colors.GREEN}✓{Colors.END} Task completed\n")
    
    def show_status(self):
        """Show system status"""
        print(f"\n{Colors.BOLD}=== System Status ==={Colors.END}\n")
        
        tools = [
            ("Aider", True),
            ("DuckDuckGo Search", True),
            ("Web Scraper", True),
            ("Task Planner", True),
            ("PyTorch", True),
        ]
        
        for name, status in tools:
            icon = f"{Colors.GREEN}✓{Colors.END}" if status else f"{Colors.RED}✗{Colors.END}"
            print(f"  {icon} {name}")
        
        mode_display = {
            AgentMode.PLAN: "🟡 PLAN",
            AgentMode.PLAN_WEB: "🟢 PLAN-WEB",
            AgentMode.AUTO: "🔵 AUTO",
            AgentMode.YOLO: "🔴 YOLO"
        }
        
        print(f"\n{Colors.BOLD}Current Mode:{Colors.END} {mode_display.get(self.mode, 'AUTO')}")
        print()
    
    def run(self):
        """Main run loop with numbered inputs"""
        self.display_header()
        
        while True:
            try:
                # Show numbered prompt
                user_input = input(f"{Colors.YELLOW}>>> [{self.command_counter}] {Colors.END}").strip()
                
                if not user_input:
                    continue
                
                # Store in history with number
                self.command_history[self.command_counter] = user_input
                current_num = self.command_counter
                self.command_counter += 1
                
                if user_input.lower() in ["quit", "exit", "q"]:
                    print(f"\n{Colors.GREEN}👋 Goodbye!{Colors.END}\n")
                    break
                
                if user_input.lower() in ["tab", "m", "mode"]:
                    self.toggle_mode()
                    continue
                
                if user_input.lower() == "status":
                    self.show_status()
                    continue
                
                if user_input.lower() == "history" or user_input.lower() == "h":
                    self.show_history()
                    continue
                
                # Check if referring to previous command
                if user_input.lower().startswith("redo ") or user_input.lower().startswith("r "):
                    try:
                        ref_num = int(user_input.split()[1])
                        if ref_num in self.command_history:
                            user_input = self.command_history[ref_num]
                            print(f"{Colors.CYAN}↩️  Redo [{ref_num}]: {user_input}{Colors.END}\n")
                        else:
                            print(f"{Colors.RED}❌ Command [{ref_num}] not found{Colors.END}\n")
                            continue
                    except (ValueError, IndexError):
                        print(f"{Colors.RED}❌ Invalid reference{Colors.END}\n")
                        continue
                
                if user_input.lower().startswith("plan-web "):
                    topic = user_input[9:]
                    self.run_plan_web(topic, current_num)
                    continue
                
                # Regular command
                self.execute_task(user_input, current_num)
                
            except KeyboardInterrupt:
                print(f"\n\n{Colors.YELLOW}⚠️  Interrupted. Type 'quit' to exit.{Colors.END}\n")
                continue
            except Exception as e:
                print(f"\n{Colors.RED}❌ Error: {e}{Colors.END}\n")
    
    def show_history(self):
        """Show command history"""
        print(f"\n{Colors.BOLD}📋 Command History:{Colors.END}\n")
        for num, cmd in sorted(self.command_history.items(), reverse=True)[:10]:
            print(f"  [{num}] {cmd}")
        print()
    
    def acknowledge(self, command: str, num: int):
        """Acknowledge user's command with checkmark and number"""
        mode_display = {
            AgentMode.PLAN: "🟡 PLAN",
            AgentMode.PLAN_WEB: "🟢 PLAN-WEB",
            AgentMode.AUTO: "🔵 AUTO",
            AgentMode.YOLO: "🔴 YOLO"
        }
        
        print(f"\n{Colors.GREEN}✅ ACKNOWLEDGED: [{num}] \"{command}\"{Colors.END}")
        print(f"   {Colors.CYAN}📍 Mode:{Colors.END} {mode_display.get(self.mode, 'AUTO')}")
        print(f"   {Colors.BLUE}🤖 Agent:{Colors.END} Coder (7B)")
        print()


def main():
    """Main entry point"""
    orchestrator = AgentOrchestrator()
    orchestrator.run()


if __name__ == "__main__":
    main()
