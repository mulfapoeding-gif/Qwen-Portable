"""
QWEN PRO - Unified AI Orchestrator
One window for everything!
"""

import sys
import time
from datetime import datetime
import os

# Colors
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Clear screen
def clear():
    print('\033[2J\033[H', end='')
    sys.stdout.flush()

# Move cursor
def move_cursor(row, col):
    print(f'\033[{row};{col}H', end='')
    sys.stdout.flush()

class UnifiedOrchestrator:
    def __init__(self):
        self.mode = "AUTO"
        self.modes = ["PLAN", "PLAN-WEB", "AUTO", "YOLO"]
        self.mode_index = 1
        self.task_num = 0
        self.history = []
        self.running = True
        
    def draw_header(self):
        """Draw top header with mode and status"""
        now = datetime.now().strftime('%H:%M:%S')
        
        print(f'{Colors.BOLD}{Colors.CYAN}╔' + '═' * 76 + '╗{Colors.END}')
        print(f'{Colors.BOLD}{Colors.CYAN}║{Colors.END}           {Colors.BOLD}🤖 QWEN PRO - Unified AI Orchestrator{Colors.END}                      {Colors.BOLD}{Colors.CYAN}║{Colors.END}')
        print(f'{Colors.BOLD}{Colors.CYAN}╠' + '═' * 76 + '╣{Colors.END}')
        print(f'{Colors.BOLD}{Colors.CYAN}║{Colors.END}  {Colors.YELLOW}📍 MODE:{Colors.END} [{self.mode:8}]  |  {Colors.BLUE}📊 Task:{Colors.END} [{self.task_num:2}]  |  {Colors.GREEN}⏰ {now}{Colors.END}                    {Colors.BOLD}{Colors.CYAN}║{Colors.END}')
        print(f'{Colors.BOLD}{Colors.CYAN}╠' + '═' * 76 + '╣{Colors.END}')
    
    def draw_output_area(self, output_lines):
        """Draw main output area"""
        print(f'{Colors.BOLD}{Colors.CYAN}║{Colors.END}  {Colors.UNDERLINE}OUTPUT AREA (Live updates):{Colors.END}                                    {Colors.BOLD}{Colors.CYAN}║{Colors.END}')
        print(f'{Colors.BOLD}{Colors.CYAN}║{Colors.END}                                                                      {Colors.BOLD}{Colors.CYAN}║{Colors.END}')
        
        # Show last 8 lines of output
        display_lines = output_lines[-8:] if len(output_lines) > 8 else output_lines
        for line in display_lines:
            # Truncate long lines
            if len(line) > 70:
                line = line[:67] + '...'
            print(f'{Colors.BOLD}{Colors.CYAN}║{Colors.END}  {line:<70} {Colors.BOLD}{Colors.CYAN}║{Colors.END}')
        
        # Fill remaining space
        remaining = 8 - len(display_lines)
        for i in range(remaining):
            print(f'{Colors.BOLD}{Colors.CYAN}║{Colors.END}                                                                      {Colors.BOLD}{Colors.CYAN}║{Colors.END}')
        
        print(f'{Colors.BOLD}{Colors.CYAN}╠' + '═' * 76 + '╣{Colors.END}')
    
    def draw_quick_actions(self):
        """Draw quick actions bar"""
        print(f'{Colors.BOLD}{Colors.CYAN}║{Colors.END}  {Colors.UNDERLINE}QUICK ACTIONS:{Colors.END}                                                      {Colors.BOLD}{Colors.CYAN}║{Colors.END}')
        print(f'{Colors.BOLD}{Colors.CYAN}║{Colors.END}    {Colors.YELLOW}[F1]{Colors.END} Help     {Colors.YELLOW}[F2]{Colors.END} History   {Colors.YELLOW}[F3]{Colors.END} Modes     {Colors.YELLOW}[F4]{Colors.END} Models         {Colors.BOLD}{Colors.CYAN}║{Colors.END}')
        print(f'{Colors.BOLD}{Colors.CYAN}║{Colors.END}    {Colors.YELLOW}[F5]{Colors.END} Search   {Colors.YELLOW}[F6]{Colors.END} Backup    {Colors.YELLOW}[F7]{Colors.END} Optimize  {Colors.YELLOW}[F8]{Colors.END} Clear          {Colors.BOLD}{Colors.CYAN}║{Colors.END}')
        print(f'{Colors.BOLD}{Colors.CYAN}╠' + '═' * 76 + '╣{Colors.END}')
    
    def draw_history(self):
        """Draw command history"""
        print(f'{Colors.BOLD}{Colors.CYAN}║{Colors.END}  {Colors.UNDERLINE}COMMAND HISTORY (Last 5):{Colors.END}                                        {Colors.BOLD}{Colors.CYAN}║{Colors.END}')
        print(f'{Colors.BOLD}{Colors.CYAN}║{Colors.END}                                                                      {Colors.BOLD}{Colors.CYAN}║{Colors.END}')
        
        # Show last 5 commands
        display_history = self.history[-5:] if len(self.history) > 5 else self.history
        for i, cmd in enumerate(reversed(display_history)):
            num = self.task_num - i
            print(f'{Colors.BOLD}{Colors.CYAN}║{Colors.END}    [{num:2}] {cmd:<62} {Colors.BOLD}{Colors.CYAN}║{Colors.END}')
        
        remaining = 5 - len(display_history)
        for i in range(remaining):
            print(f'{Colors.BOLD}{Colors.CYAN}║{Colors.END}                                                                      {Colors.BOLD}{Colors.CYAN}║{Colors.END}')
        
        print(f'{Colors.BOLD}{Colors.CYAN}╠' + '═' * 76 + '╣{Colors.END}')
    
    def draw_status(self):
        """Draw status bar"""
        print(f'{Colors.BOLD}{Colors.CYAN}║{Colors.END}  {Colors.UNDERLINE}STATUS:{Colors.END}                                                              {Colors.BOLD}{Colors.CYAN}║{Colors.END}')
        print(f'{Colors.BOLD}{Colors.CYAN}║{Colors.END}    {Colors.GREEN}🟢{Colors.END} LM Studio: Connected  |  {Colors.GREEN}🟢{Colors.END} Ollama: Ready  |  {Colors.GREEN}🟢{Colors.END} GPU: Active           {Colors.BOLD}{Colors.CYAN}║{Colors.END}')
        print(f'{Colors.BOLD}{Colors.CYAN}╠' + '═' * 76 + '╣{Colors.END}')
    
    def draw_input(self, current_input):
        """Draw input line"""
        print(f'{Colors.BOLD}{Colors.CYAN}║{Colors.END}  {Colors.BOLD}>>> {current_input}{Colors.END}                                                     {Colors.BOLD}{Colors.CYAN}║{Colors.END}')
        print(f'{Colors.BOLD}{Colors.CYAN}╚' + '═' * 76 + '╝{Colors.END}')
    
    def draw_screen(self, output_lines=[], current_input=''):
        """Draw complete screen"""
        clear()
        self.draw_header()
        self.draw_output_area(output_lines)
        self.draw_quick_actions()
        self.draw_history()
        self.draw_status()
        self.draw_input(current_input)
    
    def toggle_mode(self):
        """Toggle between modes"""
        self.mode_index = (self.mode_index + 1) % len(self.modes)
        self.mode = self.modes[self.mode_index]
    
    def add_to_history(self, command):
        """Add command to history"""
        self.history.append(command)
        if len(self.history) > 20:
            self.history.pop(0)
    
    def acknowledge(self, command):
        """Acknowledge a command"""
        self.task_num += 1
        self.add_to_history(command)
        return [
            f'{Colors.GREEN}+{Colors.END} ACKNOWLEDGED: [{self.task_num}] "{command}"',
            f'  Mode: [{self.mode:8}]  |  Agent: Coder (7B)',
        ]
    
    def show_progress(self, percent):
        """Show progress bar"""
        bar_length = 40
        filled = int(bar_length * percent / 100)
        bar = '#' * filled + '-' * (bar_length - filled)
        return f'[{bar}] {percent:3d}%'
    
    def run(self):
        """Main run loop"""
        output_lines = [
            f'{Colors.CYAN}Welcome to QWEN PRO - Unified AI Orchestrator!{Colors.END}',
            f'{Colors.YELLOW}Type commands, press Enter to execute{Colors.END}',
            f'{Colors.YELLOW}Press TAB or 'm' to toggle mode{Colors.END}',
            f'{Colors.YELLOW}Press 'q' or 'quit' to exit{Colors.END}',
        ]
        
        current_input = ''
        
        while self.running:
            self.draw_screen(output_lines, current_input)
            
            # Simple input handling
            try:
                user_input = input(f'{Colors.BOLD}{Colors.CYAN}║{Colors.END}  >>> ').strip()
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    output_lines.append(f'{Colors.YELLOW}Goodbye!{Colors.END}')
                    self.draw_screen(output_lines)
                    break
                
                if user_input.lower() in ['tab', 'm', 'mode']:
                    self.toggle_mode()
                    output_lines.append(f'{Colors.CYAN}Mode changed to: [{self.mode}]{Colors.END}')
                    continue
                
                if user_input.lower() == 'h':
                    output_lines.append(f'{Colors.CYAN}Command History:{Colors.END}')
                    for i, cmd in enumerate(self.history[-5:], 1):
                        output_lines.append(f'  [{i}] {cmd}')
                    continue
                
                if not user_input:
                    continue
                
                # Process command
                ack_lines = self.acknowledge(user_input)
                output_lines.extend(ack_lines)
                
                # Simulate progress
                for i in range(0, 101, 20):
                    output_lines.append(f'{self.show_progress(i)} Processing...')
                    self.draw_screen(output_lines)
                    time.sleep(0.2)
                    output_lines.pop()
                
                output_lines.append(f'{Colors.GREEN}+ Task [{self.task_num}] Complete!{Colors.END}')
                output_lines.append('')
                
            except KeyboardInterrupt:
                output_lines.append(f'{Colors.YELLOW}Interrupted. Type 'quit' to exit.{Colors.END}')
            except EOFError:
                break

def main():
    print(f'{Colors.BOLD}{Colors.CYAN}Starting QWEN PRO - Unified AI Orchestrator...{Colors.END}\n')
    time.sleep(1)
    
    orchestrator = UnifiedOrchestrator()
    orchestrator.run()

if __name__ == '__main__':
    main()
