"""
QWEN PRO - Unified Orchestrator (ASCII Version)
Works on all terminals - no Unicode issues!
"""

import sys
import time
import subprocess
import os
from datetime import datetime

class Colors:
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

def clear():
    print('\033[2J\033[H', end='')
    sys.stdout.flush()

class UnifiedOrchestrator:
    def __init__(self):
        self.mode = "AUTO"
        self.modes = ["PLAN", "PLAN-WEB", "AUTO", "YOLO"]
        self.mode_index = 1
        self.task_num = 0
        self.history = []
        self.running = True
        
        self.ollama_running = False
        self.llamacpp_running = False
        self.lmstudio_running = False
        
        self.check_services()
    
    def check_services(self):
        try:
            result = subprocess.run(
                ["C:\\Users\\mulfa\\AppData\\Local\\Programs\\Ollama\\ollama.exe", "list"],
                capture_output=True, timeout=5
            )
            self.ollama_running = (result.returncode == 0)
        except:
            self.ollama_running = False
        
        try:
            result = subprocess.run(["lms", "server", "status"], capture_output=True, timeout=5)
            self.lmstudio_running = ("running" in result.stdout.decode().lower())
        except:
            self.lmstudio_running = False
        
        llamacpp_path = r"C:\Users\mulfa\AppData\Local\Microsoft\WinGet\Packages\ggml.llamacpp_Microsoft.Winget.Source_8wekyb3d8bbwe\llama-server.exe"
        self.llamacpp_running = os.path.exists(llamacpp_path)
    
    def draw_header(self):
        now = datetime.now().strftime('%H:%M:%S')
        
        print('=' * 80)
        print('        QWEN PRO - Unified AI Orchestrator + Ollama + llama.cpp')
        print('=' * 80)
        print(f'  MODE: [{self.mode:8}]  |  Task: [{self.task_num:2}]  |  Time: {now}')
        print('=' * 80)
    
    def draw_services(self):
        ollama = 'Running' if self.ollama_running else 'Stopped'
        llamacpp = 'Ready' if self.llamacpp_running else 'Not found'
        lmstudio = 'Running' if self.lmstudio_running else 'Stopped'
        
        print(f'  SERVICES: Ollama: {ollama}  |  llama.cpp: {llamacpp}  |  LM Studio: {lmstudio}')
        print('=' * 80)
    
    def draw_output_area(self, output_lines):
        print('  OUTPUT AREA (Live updates):')
        print('  ' + '-' * 74)
        
        display_lines = output_lines[-8:] if len(output_lines) > 8 else output_lines
        for line in display_lines:
            if len(line) > 72:
                line = line[:69] + '...'
            print(f'  {line}')
        
        remaining = 8 - len(display_lines)
        for i in range(remaining):
            print('  ')
        
        print('=' * 80)
    
    def draw_quick_actions(self):
        print('  QUICK ACTIONS:')
        print('    [1] Qwen    [2] Ollama    [3] llama.cpp  [4] Models')
        print('    [5] Search  [6] Optimize  [7] Benchmark  [8] Help')
        print('    [9] Download HF Model  [0] Import to Ollama')
        print('=' * 80)
    
    def draw_history(self):
        print('  COMMAND HISTORY (Last 5):')
        
        display_history = self.history[-5:] if len(self.history) > 5 else self.history
        for i, cmd in enumerate(reversed(display_history)):
            num = self.task_num - i
            print(f'    [{num:2}] {cmd}')
        
        remaining = 5 - len(display_history)
        for i in range(remaining):
            print('    ')
        
        print('=' * 80)
    
    def draw_status(self):
        print('  SYSTEM STATUS:')
        print('    GPU: Quadro P1000 (Vulkan)  |  Python: 3.12  |  Git: Ready')
        print('=' * 80)
    
    def draw_input(self, current_input):
        print(f'  >>> {current_input}', end='', flush=True)
    
    def draw_screen(self, output_lines=[], current_input=''):
        clear()
        self.draw_header()
        self.draw_services()
        self.draw_output_area(output_lines)
        self.draw_quick_actions()
        self.draw_history()
        self.draw_status()
        self.draw_input(current_input)
        print()
    
    def toggle_mode(self):
        self.mode_index = (self.mode_index + 1) % len(self.modes)
        self.mode = self.modes[self.mode_index]
    
    def add_to_history(self, command):
        self.history.append(command)
        if len(self.history) > 20:
            self.history.pop(0)
    
    def acknowledge(self, command):
        self.task_num += 1
        self.add_to_history(command)
        return [
            f'+ ACKNOWLEDGED: [{self.task_num}] "{command}"',
            f'  Mode: [{self.mode:8}]  |  Agent: Coder (7B)',
        ]
    
    def show_progress(self, percent):
        bar_length = 40
        filled = int(bar_length * percent / 100)
        bar = '#' * filled + '-' * (bar_length - filled)
        return f'[{bar}] {percent:3d}%'
    
    def start_ollama(self):
        output_lines = ['Starting Ollama server...']
        try:
            subprocess.Popen(
                ["C:\\Users\\mulfa\\AppData\\Local\\Programs\\Ollama\\ollama.exe", "serve"],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
            output_lines.append('OK: Ollama server started!')
            self.ollama_running = True
        except Exception as e:
            output_lines.append(f'FAILED: {e}')
        return output_lines
    
    def start_llamacpp(self):
        output_lines = ['Starting llama.cpp server with Bootes Qwen3 Coder...']
        llamacpp_path = r"C:\Users\mulfa\AppData\Local\Microsoft\WinGet\Packages\ggml.llamacpp_Microsoft.Winget.Source_8wekyb3d8bbwe\llama-server.exe"
        # Use Bootes Qwen3 Coder for fast chatting and tasking!
        model_path = r"C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\bootes-qwen3_coder-reasoning-q4_k_m.gguf"
        
        try:
            subprocess.Popen(
                [llamacpp_path, "-m", model_path, "-ngl", "99", "-c", "4096", "--batch-size", "512", "--port", "8080"],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
            output_lines.append('OK: llama.cpp server started!')
            output_lines.append('Model: Bootes Qwen3 Coder 4B (FAST!)')
            output_lines.append('Port: 8080')
            self.llamacpp_running = True
        except Exception as e:
            output_lines.append(f'FAILED: {e}')
        return output_lines
    
    def import_to_ollama(self):
        output_lines = ['Import model to Ollama...']
        output_lines.append('Usage: ollama create MODELNAME -f Modelfile')
        output_lines.append('')
        output_lines.append('Example for Bootes Qwen3:')
        output_lines.append('  cat > Modelfile << EOF')
        output_lines.append('  FROM C:/Users/mulfa/.lmstudio/models/.../bootes-qwen3_coder-reasoning-q4_k_m.gguf')
        output_lines.append('  PARAMETER num_ctx 4096')
        output_lines.append('  PARAMETER temperature 0.7')
        output_lines.append('  SYSTEM "You are an expert coding assistant."')
        output_lines.append('  EOF')
        output_lines.append('')
        output_lines.append('  ollama create qwen3-coder -f Modelfile')
        return output_lines
    
    def run(self):
        output_lines = [
            'Welcome to QWEN PRO - Unified AI Orchestrator!',
            'Type commands, press Enter to execute',
            '[1] Qwen  [2] Ollama  [3] llama.cpp  [4] Models',
            '[5] Search  [6] Optimize  [7] Benchmark  [8] Help',
            '[9] Download HF Model  [0] Import to Ollama',
            'Type q or quit to exit',
        ]
        
        current_input = ''
        
        while self.running:
            self.draw_screen(output_lines, current_input)
            
            try:
                user_input = input().strip()
                
                # Handle quick action keys (single digits)
                if user_input in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    output_lines.append(f'>>> {user_input}')
                else:
                    output_lines.append(f'>>> {user_input}')
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    output_lines.append('Goodbye!')
                    self.draw_screen(output_lines)
                    break
                
                if user_input.lower() in ['tab', 'm', 'mode']:
                    self.toggle_mode()
                    output_lines.append(f'Mode changed to: [{self.mode}]')
                    continue
                
                if user_input == '1':
                    output_lines.append('Launching Qwen...')
                    continue
                
                if user_input == '2':
                    if self.ollama_running:
                        output_lines.append('Ollama is already running!')
                    else:
                        output_lines = self.start_ollama()
                    continue
                
                if user_input == '3':
                    if self.llamacpp_running:
                        output_lines.append('llama.cpp is ready!')
                    else:
                        output_lines = self.start_llamacpp()
                    continue
                
                if user_input == '4':
                    output_lines.append('Your Models:')
                    output_lines.append('  - LFM2-1.2B-Q8_0.gguf (FASTEST)')
                    output_lines.append('  - qwen-coder-unlimited.q4_k_m.gguf')
                    output_lines.append('  - bootes-qwen3_coder-reasoning-q4_k_m.gguf')
                    output_lines.append('  - mycopilot-codellama.gguf (8B)')
                    continue
                
                if user_input == '5':
                    output_lines.append('Search command: ai-search "query"')
                    continue
                
                if user_input == '6':
                    output_lines.append('Optimize: ai-tools\\optimize-all-models.bat')
                    continue
                
                if user_input == '7':
                    output_lines.append('Benchmark: ai-tools\\benchmark-all.bat')
                    continue
                
                if user_input == '8':
                    output_lines.append('Help: See docs/UNIFIED-FULL-GUIDE.md')
                    continue
                
                if user_input == '9':
                    output_lines.append('HuggingFace Model Downloader:')
                    output_lines.append('')
                    output_lines.append('Usage: hf-download-bodaay MODEL_ID')
                    output_lines.append('')
                    output_lines.append('Examples:')
                    output_lines.append('  hf-download-bodaay Nerdsking/Nerdsking-python-coder-7B-i')
                    output_lines.append('  hf-download-bodaay deepseek-ai/deepseek-coder-6.7b-instruct')
                    output_lines.append('  hf-download-bodaay microsoft/phi-2')
                    output_lines.append('')
                    output_lines.append('Downloads to: C:\\Users\\mulfa\\.lmstudio\\models\\imported-models\\uncategorized\\')
                    continue
                
                if user_input == '0':
                    output_lines = self.import_to_ollama()
                    continue
                
                if user_input.lower() == 'h':
                    output_lines.append('Command History:')
                    for i, cmd in enumerate(self.history[-5:], 1):
                        output_lines.append(f'  [{i}] {cmd}')
                    continue
                
                if not user_input:
                    continue
                
                ack_lines = self.acknowledge(user_input)
                output_lines.extend(ack_lines)
                
                for i in range(0, 101, 20):
                    output_lines.append(f'{self.show_progress(i)} Processing...')
                    self.draw_screen(output_lines)
                    time.sleep(0.15)
                    output_lines.pop()
                
                output_lines.append('+ Task Complete!')
                output_lines.append('')
                
            except KeyboardInterrupt:
                output_lines.append('Interrupted. Type quit to exit.')
            except EOFError:
                break

def main():
    print('Starting QWEN PRO - Unified AI Orchestrator...\n')
    time.sleep(1)
    
    orchestrator = UnifiedOrchestrator()
    orchestrator.run()

if __name__ == '__main__':
    main()
