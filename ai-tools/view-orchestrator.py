"""
Qwen Orchestrator - Quick View
Shows what you see when you type 'qwen'
"""

print("""
================================================================
  Qwen Orchestrator - What You See When You Type 'qwen'
================================================================

+--------------------------------------------------------------+
|     SAFE WORKSPACE - AI Agent Environment                    |
+--------------------------------------------------------------+
|  Protected Environment:                                      |
|    + Git auto-commit                                         |
|    + Automatic backups                                       |
|    + Protected directories                                   |
|    + Activity logging                                        |
|                                                              |
|  Commands:                                                   |
|    - Type your command                                       |
|    - TAB or 'm' = Toggle mode                                |
|    - 'backup' = Manual backup                                |
|    - 'status' = Show status                                  |
|    - 'quit' = Exit                                           |
+--------------------------------------------------------------+

EXAMPLE SESSION:
================================================================

>>> [1] create a python function

+ ACKNOWLEDGED: [1] "create a python function"
  Mode: [AUTO]
  Agent: Coder (7B)

[----------------------------------------]   0% Generating code...
[############----------------------------]  30%
[########################----------------]  60%
[########################################] 100%

+ Task [1] Complete!

Result:
  def hello():
      print("Hello, World!")

>>> [2] h

Command History:
  [  2] h
  [  1] create a python function

>>> [3] r 1

Redo [1]: create a python function

+ ACKNOWLEDGED: [3] "create a python function"
  Mode: [AUTO]

================================================================

TO SEE IT LIVE:

  1. Open NEW PowerShell window
  2. Type: qwen
  3. Start typing commands
  4. Watch the indicators!

OR Run the demo:
  py -3.12 qwen-orchestrator-display.py

================================================================
""")

input("Press Enter to exit...")
