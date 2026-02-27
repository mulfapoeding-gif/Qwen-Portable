"""
Gradio Dashboard for AI Agent Analytics
========================================
Interactive UI to monitor and control AI agents
"""

import gradio as gr
import subprocess
import json
from datetime import datetime

# Store conversation history
conversation_history = []

def run_aider_command(message):
    """Run aider with a message and return output"""
    try:
        cmd = [
            "py", "-3.12", "-m", "aider",
            "--openai-api-base", "http://localhost:1234/v1",
            "--openai-api-key", "not-needed",
            "--message", message,
            "--exit"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        return result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return "⚠️ Command timed out"
    except Exception as e:
        return f"❌ Error: {e}"

def search_web(query):
    """Run DuckDuckGo search"""
    try:
        cmd = ["ddgs", query, "-m", "5"]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        return result.stdout if result.stdout else "No results found"
    except Exception as e:
        return f"❌ Search error: {e}"

def chat_with_agent(message, history):
    """Simple chat interface"""
    conversation_history.append({
        "timestamp": datetime.now().isoformat(),
        "user": message,
        "agent": "Response pending..."
    })
    
    response = run_aider_command(message)
    
    conversation_history[-1]["agent"] = response
    
    return response

def get_analytics():
    """Return conversation analytics"""
    if not conversation_history:
        return "No conversations yet"
    
    stats = {
        "total_conversations": len(conversation_history),
        "recent": conversation_history[-5:] if len(conversation_history) > 5 else conversation_history
    }
    
    return json.dumps(stats, indent=2)

def check_lmstudio_status():
    """Check if LM Studio server is running"""
    try:
        import requests
        response = requests.get("http://localhost:1234/v1/models", timeout=5)
        if response.status_code == 200:
            return "🟢 LM Studio is running"
        return "🟡 LM Studio responded but may have issues"
    except:
        return "🔴 LM Studio is not running - start the server!"

# Create Gradio interface
with gr.Blocks(title="AI Agent Dashboard", theme=gr.themes.Soft()) as dashboard:
    gr.Markdown("# 🤖 AI Agent Control Dashboard")
    
    with gr.Row():
        with gr.Column(scale=2):
            gr.Markdown("### 💬 Chat with Agent")
            chatbot = gr.ChatInterface(
                chat_with_agent,
                examples=[
                    "Explain what Aider does",
                    "How do I create a Kotlin Android project?",
                    "What is Gradle?"
                ]
            )
        
        with gr.Column(scale=1):
            gr.Markdown("### 📊 Status & Analytics")
            
            status_btn = gr.Button("Check LM Studio Status")
            status_output = gr.Textbox(label="Server Status")
            status_btn.click(check_lmstudio_status, outputs=status_output)
            
            analytics_btn = gr.Button("Get Analytics")
            analytics_output = gr.Textbox(label="Conversation Stats")
            analytics_btn.click(get_analytics, outputs=analytics_output)
            
            gr.Markdown("### 🔍 Quick Search")
            search_input = gr.Textbox(
                label="Search Query",
                placeholder="Enter search term..."
            )
            search_btn = gr.Button("Search")
            search_output = gr.Textbox(label="Search Results", lines=10)
            search_btn.click(search_web, inputs=search_input, outputs=search_output)
    
    gr.Markdown("""
    ---
    **Tools Available:**
    - **Aider**: AI pair programming (uses LM Studio)
    - **DuckDuckGo**: Web search for research
    - **LangChain**: Build custom agent workflows
    - **AutoGen**: Multi-agent conversations
    """)

if __name__ == "__main__":
    dashboard.launch()
