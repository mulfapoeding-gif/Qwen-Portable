"""
Qwen Orchestrator - Visual Task Display (ASCII Version)
Shows all indicators - works on all terminals
"""

import sys
import time

class Colors:
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    END = '\033[0m'

SPINNER = ['|', '/', '-', '\\']

def acknowledge_task(task_num, command, mode="AUTO"):
    mode_icons = {"PLAN": "[PLAN]", "PLAN-WEB": "[WEB]", "AUTO": "[AUTO]", "YOLO": "[YOLO]"}
    print(f"\n{Colors.GREEN}+{Colors.END} ACKNOWLEDGED: [{task_num}] \"{command}\"")
    print(f"  Mode: {mode_icons.get(mode, '[AUTO]')}")
    print(f"  Agent: Coder (7B)")

def show_progress(percent=0):
    bar_length = 40
    filled = int(bar_length * percent / 100)
    bar = '#' * filled + '-' * (bar_length - filled)
    sys.stdout.write(f'\r[{bar}] {percent:3d}%')
    sys.stdout.flush()

def animate_spinner(message, duration=1.5):
    start = time.time()
    idx = 0
    while time.time() - start < duration:
        spinner = SPINNER[idx % len(SPINNER)]
        sys.stdout.write(f'\r{spinner} {message}')
        sys.stdout.flush()
        time.sleep(0.1)
        idx += 1
    print(f'\r  {message}                    ')

print("""
================================================================
  QWEN ORCHESTRATOR - Visual Task Display
  (Mostly for indication on tasking)
================================================================
""")

print("+--------------------------------------------------------------+")
print("|  Modes: [PLAN]  [PLAN-WEB]  [AUTO]  [YOLO]                   |")
print("|  Input: [number] command                                     |")
print("|  History: h | Redo: r [number]                               |")
print("+--------------------------------------------------------------+")

print("\n1. TASK ACKNOWLEDGMENT")
print("--------------------------------------------------------------")
acknowledge_task(1, "create a python function", "AUTO")
acknowledge_task(2, "add error handling", "AUTO")
acknowledge_task(3, "write unit tests", "PLAN-WEB")

print("\n2. PROGRESS BARS")
print("--------------------------------------------------------------")
for i in range(0, 101, 10):
    show_progress(i)
    time.sleep(0.15)
print()

print("\n3. LOADING SPINNERS")
print("--------------------------------------------------------------")
animate_spinner("Loading model...", 1.0)
animate_spinner("Processing request...", 1.0)
animate_spinner("Generating response...", 1.0)

print("\n4. MODE INDICATORS")
print("--------------------------------------------------------------")
print("  [PLAN]       - Show what would be done")
print("  [PLAN-WEB]   - Research internet + plan")
print("  [AUTO]       - Execute with confirmation")
print("  [YOLO]       - Execute immediately")

print("\n5. COMMAND HISTORY")
print("--------------------------------------------------------------")
history = {
    10: "deploy to production",
    9: "add logging",
    8: "write documentation",
    7: "refactor module",
    6: "fix bug in parser",
    5: "add error handling",
    4: "create main function",
    3: "add tests",
    2: "refactor code",
    1: "create a python function"
}
print("\nCommand History:\n")
for num, cmd in sorted(history.items(), reverse=True):
    print(f"  [{num:3d}] {cmd}")

print("\n6. TASK COMPLETION")
print("--------------------------------------------------------------")
print("""
+==============================================================+
  Task [1] Complete!

  Result:
    def hello():
        print('Hello, World!')
    
    # Usage:
    hello()
+==============================================================+
""")

print("""
================================================================
  To use in real orchestrator:
    1. Type: qwen
    2. Commands are numbered automatically
    3. Use 'h' to see history
    4. Use 'r [number]' to redo tasks
================================================================
""")
