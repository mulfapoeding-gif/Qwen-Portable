# Qwen Agent Orchestrator Guide

## 🎯 What It Does

The **Orchestrator** is your unified command center that:

1. **Listens** for your commands
2. **Selects** the right agents automatically
3. **Shows indicators** while agents work
4. **Returns** combined results

```
You: "Create a Python function to sort a list"
       ↓
┌──────────────────────────────────────┐
│  📍 Mode: AUTO                       │
├──────────────────────────────────────┤
│  Step 1/2: Activating aider agent... │
│  [████████████░░░░░░░░] Running...   │
│  ✓ aider completed                   │
│                                      │
│  Step 2/2: Activating autogen...     │
│  [████████████████████] Running...   │
│  ✓ autogen completed                 │
└──────────────────────────────────────┘
       ↓
Result: Code + Review from both agents
```

---

## 🚀 Quick Start

### Method 1: Batch File (Easiest)
```bash
qwen-agent.bat
```

### Method 2: Direct Python
```bash
py -3.12 examples\qwen_orchestrator.py
```

---

## 🎛️ Modes (Tab Key Toggle)

Press **TAB** or type **`m`** to cycle through modes:

### 🟡 PLAN Mode
- Shows **what would be done**
- No execution
- Safe for testing

```
>>> Create a login function

[PLAN] Would use aider to: Create a login function
[PLAN] Would use autogen to: Review the code
```

### 🔵 AUTO Mode (Default)
- **Executes** with visual indicators
- Shows progress for each agent
- You see everything happening

```
>>> Create a login function

Step 1/2: Activating aider agent...
[████████████████████] Running aider...
✓ aider completed

Step 2/2: Activating autogen...
[████████████████████] Running autogen...
✓ autogen completed
```

### 🔴 YOLO Mode
- **Execute immediately**
- No confirmations
- Fastest but least control

```
>>> Create a login function

[Running agents...]
✓ Done! Here's your code.
```

---

## 💬 Commands

| Command | Description |
|---------|-------------|
| **Any text** | Processed as command |
| `tab` or `m` | Toggle mode (Plan/Auto/Yolo) |
| `status` | Show available agents |
| `quit` or `exit` | Exit orchestrator |

---

## 📊 Visual Indicators

### Spinner Animation
```
⠋ Running aider...
⠙ Running aider...
⠹ Running aider...
⠸ Running aider...
```

### Progress Bar
```
[████████████░░░░░░░░] Step 1/3
[████████████████████] Complete ✓
```

### Status Colors
- 🟢 **Green** = Success
- 🔴 **Red** = Error
- 🟡 **Yellow** = Plan mode
- 🔵 **Blue** = Auto mode
- 🔴 **Red** = Yolo mode

---

## 🤖 Automatic Agent Selection

The orchestrator **automatically picks** which agents to use:

| Your Command | Agents Used |
|--------------|-------------|
| "Create a function..." | Aider + AutoGen |
| "Search for..." | DuckDuckGo |
| "Debug this..." | AutoGen |
| "Write code..." | Aider |
| "Explain..." | AutoGen |

### How It Works

```python
# Orchestrator analyzes your command
if "code" in command or "write" in command:
    use_agent('aider')
    
if "search" in command or "find" in command:
    use_agent('search')
    
if "review" in command or "debug" in command:
    use_agent('autogen')
```

---

## ⚙️ Customization

### Add New Agents

Edit `qwen_orchestrator.py`:

```python
async def _run_custom_agent(self, command: str) -> str:
    """Your custom agent logic"""
    # Add your code here
    return result

# Add to _select_agents method
if "custom" in command_lower:
    agents.append('custom')
```

### Change Indicators

Edit the `StatusIndicator` class:

```python
SPINNERS = ['🌑', '🌒', '🌓', '🌔', '🌕', '🌖', '🌗', '🌘']
```

### Adjust Progress Bar Size

```python
# In StatusIndicator.step method
bar = '█' * int((current / total) * 30)  # 30 chars wide
```

---

## 🔧 Integration with Your Workflow

### Example: Android Development

```
>>> Create a Kotlin Android Activity

📍 Mode: AUTO

Step 1/2: Activating aider agent...
[████████████████████] Running...
✓ aider completed
   Created MainActivity.kt

Step 2/2: Activating autogen agent...
[████████████████████] Running...
✓ autogen completed
   Code reviewed, suggestions provided

Result:
1. MainActivity.kt created
2. Review: Add null safety checks
```

### Example: Research + Code

```
>>> Search for Python async patterns and create example

Step 1/2: Activating search agent...
[████████████████████] Searching...
✓ search completed
   Found 5 relevant results

Step 2/2: Activating aider agent...
[████████████████████] Running...
✓ aider completed
   Created async_example.py

Result:
- Search results with links
- Working code example
```

---

## 🛠️ Troubleshooting

### "No agents available"
```
✗ aider
✗ autogen
✗ search

→ Start LM Studio server
→ Install DuckDuckGo: pip install duckduckgo-search
```

### Indicators not showing
- Check terminal supports ANSI colors
- Try Windows Terminal instead of cmd

### Agents not executing
- Check you're in AUTO or YOLO mode
- Type `status` to verify agents

### Slow progress
- Large models take time
- Reduce context window in LM Studio
- Use smaller models for faster response

---

## 📋 Example Session

```
╔══════════════════════════════════════════════════════════╗
║     🤖 Qwen Agent Orchestrator                        ║
╠══════════════════════════════════════════════════════════╣
║  Commands:                                               ║
║    - Type your command                                   ║
║    - TAB or 'm' = Toggle mode (Plan/Auto/Yolo)           ║
║    - 'status' = Show agent status                        ║
║    - 'quit' = Exit                                       ║
╚══════════════════════════════════════════════════════════╝

=== Agent Status ===
  ✓ Aider
  ✓ Langchain
  ✓ Autogen
  ✓ Search

>>> Create a python function to calculate fibonacci

Step 1/1: Activating aider agent...
[████████████████████] Running aider...
✓ aider completed

══════════════════════════════════════════════════════════
Results:

[1] Here's the code:

def fibonacci(n):
    """Calculate fibonacci of n"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Example usage
print(fibonacci(10))  # Output: 55

══════════════════════════════════════════════════════════

>>> m

📍 Mode: PLAN

>>> Search for async best practices

[PLAN] Would use search to: Search for async best practices
[PLAN] Would use aider to: Create examples

>>> tab

📍 Mode: YOLO

>>> Create async example

[Running agents...]
✓ Done! Here's your async code.

>>> quit

👋 Goodbye!
```

---

## 🎯 Summary

The Orchestrator gives you:

✅ **Single interface** for all agents  
✅ **Visual indicators** showing progress  
✅ **Mode switching** (Plan/Auto/Yolo)  
✅ **Automatic agent selection**  
✅ **Combined results** from multiple agents  

**Start with:** `qwen-agent.bat`

**Toggle modes:** Press `TAB` or type `m`

**See status:** Type `status`

---

**Next:** Try it out and customize for your workflow!
