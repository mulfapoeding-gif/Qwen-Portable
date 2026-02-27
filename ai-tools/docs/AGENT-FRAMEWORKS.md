# AI Agent Framework Integration Guide

## 🎯 Overview

You now have a complete AI development stack with:

| Component | Purpose | Status |
|-----------|---------|--------|
| **Aider** | AI pair programming in terminal | ✅ Installed |
| **LangChain** | Build agent workflows | ✅ Installed |
| **AutoGen** | Multi-agent conversations | ✅ Installed |
| **Gradio** | Web UI dashboards | ✅ Installed |
| **DuckDuckGo CLI** | Web research | ✅ Installed |
| **LM Studio** | Local model server | Use your existing models |

---

## 📁 File Structure

```
uncategorized/
├── AIDER-SETUP.md              # Aider setup guide
├── INSTALL-SUMMARY.md          # Installation summary
├── AGENT-FRAMEWORKS.md         # This file
├── aider-lmstudio.bat          # Aider launcher
└── examples/
    ├── langchain_agent.py      # LangChain search agent
    ├── autogen_agents.py       # AutoGen multi-agent
    └── gradio_dashboard.py     # Gradio control panel
```

---

## 🚀 Quick Start

### 1. Start LM Studio Server
```
1. Open LM Studio
2. Load a model (Qwen Coder recommended)
3. Go to "Local Server" tab
4. Click "Start Server"
```

### 2. Test Aider
```bash
py -3.12 -m aider --openai-api-base http://localhost:1234/v1 --openai-api-key not-needed
```

### 3. Run Example Agents

**LangChain Research Agent:**
```bash
cd examples
py -3.12 langchain_agent.py
```

**AutoGen Multi-Agent:**
```bash
cd examples
py -3.12 autogen_agents.py
```

**Gradio Dashboard:**
```bash
cd examples
py -3.12 gradio_dashboard.py
# Open browser to http://localhost:7860
```

---

## 🔧 Framework Details

### LangChain - Single Agent Workflows

**Best for:** Structured tasks, tool use, chains

```python
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_openai import ChatOpenAI

# Local model
llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="not-needed"
)

# Tools
search = DuckDuckGoSearchResults()
tools = [search]

# Build your agent
```

**Install:** `pip install langchain langchain-community langchain-openai`

---

### AutoGen - Multi-Agent Conversations

**Best for:** Collaborative tasks, code review, planning

```python
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat

# Create agents
coder = AssistantAgent("Coder", model_client=lmstudio_client)
reviewer = AssistantAgent("Reviewer", model_client=lmstudio_client)

# Team conversation
team = RoundRobinGroupChat([coder, reviewer])
```

**Install:** `pip install pyautogen`

---

### Gradio - Web Interfaces

**Best for:** Dashboards, user-friendly interfaces, demos

```python
import gradio as gr

def process(text):
    return f"You entered: {text}"

demo = gr.Interface(fn=process, inputs="text", outputs="text")
demo.launch()
```

**Install:** `pip install gradio`

---

## 🎛️ Tab Key Mode Switching (Custom Implementation)

The Tab key mode switching (Plan/Auto/Yolo) you mentioned isn't built into these frameworks by default, but you can implement it:

### Example: Custom Mode Switcher

```python
# Add to your agent code
import sys
import tty
import termios

class ModeSwitcher:
    PLAN = "plan"
    AUTO = "auto"
    YOLO = "yolo"
    
    def __init__(self):
        self.mode = self.PLAN
    
    def handle_key(self, key):
        if key == '\t':  # Tab key
            modes = [self.PLAN, self.AUTO, self.YOLO]
            current_idx = modes.index(self.mode)
            self.mode = modes[(current_idx + 1) % len(modes)]
            print(f"\n📍 Mode: {self.mode.upper()}")
        return self.mode
    
    def should_execute(self):
        if self.mode == self.PLAN:
            return False  # Just show plan
        elif self.mode == self.AUTO:
            return True   # Execute with confirmation
        elif self.mode == self.YOLO:
            return "YOLO" # Execute immediately
```

---

## 🔍 DuckDuckGo Search Integration

### Command Line
```bash
# Basic search
ddgs "kotlin gradle setup"

# With options
ddgs "android build errors" -m 10 -r day
```

### In Python Code
```python
from duckduckgo_search import DDGS

with DDGS() as ddgs:
    results = ddgs.text("python async tutorial", max_results=5)
    for r in results:
        print(r['title'])
        print(r['href'])
```

### In LangChain Agent
```python
from langchain_community.tools import DuckDuckGoSearchResults

search = DuckDuckGoSearchResults()
results = search.run("latest Android SDK features")
```

---

## 📊 Analytics Dashboard

The Gradio dashboard (`gradio_dashboard.py`) provides:
- LM Studio status check
- Conversation history
- Quick web search
- Agent control interface

**Customize it:**
- Add matplotlib charts for conversation analytics
- Log agent interactions to file
- Add buttons for common commands

---

## 🤝 How Tools Work Together

```
┌─────────────────────────────────────────────────────────┐
│                    Your Terminal                         │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │  Aider   │  │ LangChain│  │ AutoGen  │              │
│  │  (CLI)   │  │ (Python) │  │ (Python) │              │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘              │
│       │             │             │                     │
│       └─────────────┴─────────────┘                     │
│                     │                                   │
│              ┌──────▼──────┐                            │
│              │ LM Studio   │                            │
│              │  (Server)   │                            │
│              └──────┬──────┘                            │
│                     │                                   │
│              ┌──────▼──────┐                            │
│              │ Local Model │                            │
│              │  (Qwen, etc)│                            │
│              └─────────────┘                            │
│                                                          │
│  ┌──────────────────┐  ┌──────────────────┐            │
│  │  DuckDuckGo CLI  │  │   Gradio Web UI  │            │
│  │  (Research)      │  │   (Dashboard)    │            │
│  └──────────────────┘  └──────────────────┘            │
└─────────────────────────────────────────────────────────┘
```

---

## 🛠️ Common Workflows

### 1. Debug Build Error
```bash
# 1. Search for solution
ddgs "gradle build failed missing dependency"

# 2. Ask Aider to fix
aider build.gradle.kts -m "Fix this: <paste error>"

# 3. Use AutoGen for complex issues
py -3.12 autogen_agents.py
# Task: "Debug this gradle error: <error>"
```

### 2. Learn New Technology
```bash
# 1. Research
ddgs "Kotlin coroutines tutorial 2025"

# 2. Generate code examples
aider -m "Show me Kotlin coroutine examples for Android"

# 3. Review with multi-agent
py -3.12 autogen_agents.py
# Task: "Review this coroutine code for best practices"
```

### 3. Build Dashboard for Team
```bash
# Customize gradio_dashboard.py
# Add your team's common workflows
# Host on local network
gradio_dashboard.py
# Share http://localhost:7860 with team
```

---

## ⚙️ Configuration Tips

### LM Studio Settings
- **Context Window**: 4096+ recommended
- **Model**: Qwen Coder (7B+) for code tasks
- **Temperature**: 0.7 for creative, 0.3 for precise

### Aider Settings
Create `.aider.conf.yml` in your project:
```yaml
model: local-model
openai-api-base: http://localhost:1234/v1
openai-api-key: not-needed
auto-commits: true
dark-mode: true
```

### Environment Variables
Add to system environment:
```
AIDER_OPENAI_API_BASE=http://localhost:1234/v1
AIDER_OPENAI_API_KEY=not-needed
```

---

## 🐛 Troubleshooting

### "Connection refused"
- Start LM Studio server
- Check port (default 1234)

### "Module not found"
- Use `py -3.12 -m pip install <package>`
- Check Python version: `py -3.12 --version`

### AutoGen errors
- Ensure LM Studio supports function calling
- Some models may not work with AutoGen

### Gradio not loading
- Check firewall settings
- Try `dashboard.launch(server_name="0.0.0.0")`

---

## 📚 Next Steps

1. **Explore LangChain docs:** https://python.langchain.com/
2. **AutoGen examples:** https://microsoft.github.io/autogen/
3. **Gradio demos:** https://gradio.app/docs/
4. **Build your custom agent** with Tab mode switching
5. **Create analytics logging** for agent interactions

---

## 🎯 Summary

You now have:
- ✅ **Aider** for terminal pair programming
- ✅ **LangChain** for single-agent workflows with tools
- ✅ **AutoGen** for multi-agent collaboration
- ✅ **Gradio** for web dashboards
- ✅ **DuckDuckGo** for research
- ✅ **LM Studio** integration for all tools

**Everything works with your local Qwen models!**
