# -*- coding: utf-8 -*-
"""
Qwen Agent Orchestrator
========================
Unified command system that triggers agents with visual indicators

Usage:
    py -3.12 qwen_orchestrator.py
"""

import os
import sys
import asyncio
import time
from datetime import datetime
from enum import Enum
from typing import Optional, List, Dict

# Force UTF-8 encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Color codes for terminal output
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
    AUTO = "auto"
    YOLO = "yolo"

class StatusIndicator:
    """Shows animated status indicators while agents work"""
    
    SPINNERS = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    
    def __init__(self):
        self.current_step = 0
        self.total_steps = 0
    
    def animate(self, message: str, duration: float = 0.1):
        """Show animated spinner with message"""
        spinner = self.SPINNERS[self.current_step % len(self.SPINNERS)]
        self.current_step += 1
        sys.stdout.write(f'\r{Colors.CYAN}{spinner} {Colors.END}{message}')
        sys.stdout.flush()
        time.sleep(duration)
    
    def stop(self, success: bool = True):
        """Stop animation and show result"""
        sys.stdout.write('\r' + ' ' * 60 + '\r')
        if success:
            print(f'{Colors.GREEN}✓{Colors.END} Complete')
        else:
            print(f'{Colors.RED}✗{Colors.END} Failed')
    
    def step(self, current: int, total: int, message: str):
        """Show progress step"""
        bar = '█' * int((current / total) * 20)
        bar = bar.ljust(20, '░')
        sys.stdout.write(f'\r{Colors.BLUE}[{bar}] {Colors.END}{message}')
        sys.stdout.flush()

class AgentOrchestrator:
    """
    Main orchestrator that manages agents and shows indicators
    """
    
    def __init__(self):
        self.mode = AgentMode.PLAN
        self.status = StatusIndicator()
        self.agents_available = {
            'aider': False,
            'langchain': False,
            'autogen': False,
            'search': False,
        }
        self._check_agents()
    
    def _check_agents(self):
        """Check which agents are available"""
        import subprocess
        
        # Check LM Studio
        try:
            import requests
            r = requests.get('http://localhost:1234/v1/models', timeout=2)
            if r.status_code == 200:
                self.agents_available['aider'] = True
                self.agents_available['langchain'] = True
                self.agents_available['autogen'] = True
        except:
            pass
        
        # Check DuckDuckGo
        try:
            result = subprocess.run(['ddgs', '--version'], capture_output=True, timeout=5)
            if result.returncode == 0:
                self.agents_available['search'] = True
        except:
            pass
    
    def show_status(self):
        """Show available agents"""
        print(f"\n{Colors.BOLD}=== Agent Status ==={Colors.END}")
        for agent, available in self.agents_available.items():
            status = f"{Colors.GREEN}✓{Colors.END}" if available else f"{Colors.RED}✗{Colors.END}"
            print(f"  {status} {agent.capitalize()}")
        print()
    
    def toggle_mode(self):
        """Toggle between Plan/Auto/Yolo modes"""
        modes = list(AgentMode)
        current_idx = modes.index(self.mode)
        self.mode = modes[(current_idx + 1) % len(modes)]
        
        mode_colors = {
            AgentMode.PLAN: Colors.YELLOW,
            AgentMode.AUTO: Colors.BLUE,
            AgentMode.YOLO: Colors.RED,
        }
        
        print(f"\n{mode_colors[self.mode]}📍 Mode: {self.mode.value.upper()}{Colors.END}\n")
        return self.mode
    
    async def run_command(self, command: str) -> str:
        """
        Process a command through appropriate agents with indicators
        """
        print(f"\n{Colors.BOLD}>>> Command:{Colors.END} {command}\n")
        
        # Determine which agents to use
        agents_to_use = self._select_agents(command)
        
        if not agents_to_use:
            return "❌ No agents available. Start LM Studio server."
        
        results = []
        
        for i, agent in enumerate(agents_to_use, 1):
            print(f"\n{Colors.BOLD}Step {i}/{len(agents_to_use)}:{Colors.END} Activating {agent} agent...")
            
            # Show progress indicator
            for j in range(10):
                self.status.animate(f"Running {agent}...", 0.05)
            self.status.stop(success=True)
            
            # Execute agent
            if self.mode == AgentMode.PLAN:
                result = await self._plan_only(agent, command)
            elif self.mode == AgentMode.AUTO:
                result = await self._execute_with_confirm(agent, command)
            else:  # YOLO
                result = await self._execute_immediately(agent, command)
            
            results.append(result)
            print(f"{Colors.GREEN}✓{Colors.END} {agent} completed")
        
        # Combine results
        return self._format_results(results)
    
    def _select_agents(self, command: str) -> List[str]:
        """Select which agents to use based on command"""
        agents = []
        command_lower = command.lower()
        
        if any(word in command_lower for word in ['code', 'write', 'create', 'function', 'class']):
            if self.agents_available['aider']:
                agents.append('aider')
            if self.agents_available['autogen']:
                agents.append('autogen')
        
        if any(word in command_lower for word in ['search', 'find', 'research', 'look up']):
            if self.agents_available['search']:
                agents.append('search')
        
        if any(word in command_lower for word in ['analyze', 'review', 'debug', 'explain']):
            if self.agents_available['autogen']:
                agents.append('autogen')
        
        # Default to aider if nothing matched
        if not agents and self.agents_available['aider']:
            agents.append('aider')
        
        return agents
    
    async def _plan_only(self, agent: str, command: str) -> str:
        """PLAN mode: Just show what would be done"""
        return f"[PLAN] Would use {agent} to: {command}"
    
    async def _execute_with_confirm(self, agent: str, command: str) -> str:
        """AUTO mode: Execute but show what's happening"""
        if agent == 'aider':
            return await self._run_aider(command)
        elif agent == 'search':
            return await self._run_search(command)
        elif agent == 'autogen':
            return await self._run_autgen(command)
        return f"Executed with {agent}"
    
    async def _execute_immediately(self, agent: str, command: str) -> str:
        """YOLO mode: Execute without confirmation"""
        return await self._execute_with_confirm(agent, command)
    
    async def _run_aider(self, command: str) -> str:
        """Run Aider agent"""
        import subprocess
        try:
            cmd = [
                'py', '-3.12', '-m', 'aider',
                '--openai-api-base', 'http://localhost:1234/v1',
                '--openai-api-key', 'not-needed',
                '--message', command,
                '--exit'
            ]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return result.stdout if result.stdout else result.stderr
        except Exception as e:
            return f"Aider error: {e}"
    
    async def _run_search(self, query: str) -> str:
        """Run DuckDuckGo search"""
        import subprocess
        try:
            cmd = ['ddgs', query, '-m', '5']
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return result.stdout if result.stdout else "No results found"
        except Exception as e:
            return f"Search error: {e}"
    
    async def _run_autgen(self, command: str) -> str:
        """Run AutoGen multi-agent"""
        return f"[AutoGen] Would process: {command}\n(Use autogen_agents.py for full multi-agent)"
    
    def _format_results(self, results: List[str]) -> str:
        """Format final results"""
        print(f"\n{Colors.BOLD}{'='*60}{Colors.END}")
        print(f"{Colors.BOLD}Results:{Colors.END}")
        for i, result in enumerate(results, 1):
            print(f"\n{Colors.CYAN}[{i}]{Colors.END} {result}")
        print(f"{Colors.BOLD}{'='*60}{Colors.END}\n")
        return "\n".join(results)

async def main():
    """Main interactive loop"""
    orchestrator = AgentOrchestrator()
    
    print(f"""
{Colors.BOLD}╔══════════════════════════════════════════════════════════╗
║     🤖 Qwen Agent Orchestrator                        ║
╠══════════════════════════════════════════════════════════╣
║  Commands:                                               ║
║    - Type your command                                   ║
║    - TAB or 'm' = Toggle mode (Plan/Auto/Yolo)           ║
║    - 'status' = Show agent status                        ║
║    - 'quit' = Exit                                       ║
╚══════════════════════════════════════════════════════════╝
{Colors.END}""")
    
    orchestrator.show_status()
    
    while True:
        try:
            # Get user input
            user_input = input(f"{Colors.YELLOW}>>> {Colors.END}").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print(f"\n{Colors.GREEN}👋 Goodbye!{Colors.END}\n")
                break
            
            if user_input.lower() == 'status':
                orchestrator.show_status()
                continue
            
            if user_input.lower() in ['tab', 'm', 'mode']:
                orchestrator.toggle_mode()
                continue
            
            # Process command
            result = await orchestrator.run_command(user_input)
            
        except KeyboardInterrupt:
            print(f"\n\n{Colors.YELLOW}⚠️  Interrupted. Type 'quit' to exit.{Colors.END}\n")
            continue
        except Exception as e:
            print(f"\n{Colors.RED}❌ Error: {e}{Colors.END}\n")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n{Colors.GREEN}👋 Goodbye!{Colors.END}\n")
