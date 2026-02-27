"""
AutoGen Multi-Agent System with LM Studio
==========================================
Example: Multiple AI agents collaborating using local models
"""

import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient

# Configure LM Studio as the model client
def create_lmstudio_client():
    return OpenAIChatCompletionClient(
        model="local-model",
        base_url="http://localhost:1234/v1",
        api_key="not-needed",
        model_info={
            "vision": False,
            "function_calling": True,
            "json_output": False,
            "family": "unknown",
        },
    )

# Create specialized agents
def create_coder_agent():
    return AssistantAgent(
        name="Coder",
        description="A Python/Kotlin developer who writes code",
        model_client=create_lmstudio_client(),
        system_message="""You are a coding expert. 
When asked to write code, provide clean, well-commented code examples.
Focus on Python, Kotlin, and Android development.
""",
    )

def create_reviewer_agent():
    return AssistantAgent(
        name="Reviewer",
        description="A code reviewer who checks for bugs and improvements",
        model_client=create_lmstudio_client(),
        system_message="""You are a code reviewer.
Analyze code for:
- Bugs and potential errors
- Performance improvements  
- Best practices
- Security issues
Be constructive and helpful in your feedback.
""",
    )

def create_planner_agent():
    return AssistantAgent(
        name="Planner",
        description="Plans tasks and breaks them into steps",
        model_client=create_lmstudio_client(),
        system_message="""You are a task planner.
Break down complex requests into clear, actionable steps.
Help organize work logically before coding begins.
""",
    )

async def run_multi_agent():
    """Run the multi-agent collaboration system"""
    print("=== AutoGen Multi-Agent System ===")
    print("Agents: Planner → Coder → Reviewer")
    print("Make sure LM Studio server is running on http://localhost:1234")
    print()
    
    # Create agents
    planner = create_planner_agent()
    coder = create_coder_agent()
    reviewer = create_reviewer_agent()
    
    # Create team with round-robin conversation
    team = RoundRobinGroupChat(
        [planner, coder, reviewer],
        max_turns=6,  # Limit conversation turns
    )
    
    while True:
        user_input = input("\nYour task: ").strip()
        if user_input.lower() in ["quit", "exit", "q"]:
            break
        
        print("\n🤖 Agents working...\n")
        print("=" * 50)
        
        # Run the team
        stream = team.run_stream(task=user_input)
        async for message in stream:
            if hasattr(message, 'content') and message.content:
                print(f"\n{message.source}: {message.content}")
        
        print("=" * 50)
        print("✅ Task complete!\n")

if __name__ == "__main__":
    asyncio.run(run_multi_agent())
