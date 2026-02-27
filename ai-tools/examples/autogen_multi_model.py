"""
AutoGen Multi-Agent with Multiple Models
=========================================
Run 2+ agents with DIFFERENT models working together

OPTIONS:
1. Multiple LM Studio instances (ports 1234, 1235)
2. LM Studio + Ollama (ports 1234, 11434)
3. Single model, different system prompts
"""

import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient

# ============ CONFIGURATION ============

# Option A: Two LM Studio instances (requires 2 LM Studio windows)
CODER_MODEL_CLIENT = OpenAIChatCompletionClient(
    model="local-model",
    base_url="http://localhost:1234/v1",  # LM Studio Instance 1
    api_key="not-needed",
    model_info={"vision": False, "function_calling": True, "json_output": False, "family": "unknown"},
)

REVIEWER_MODEL_CLIENT = OpenAIChatCompletionClient(
    model="local-model",
    base_url="http://localhost:1235/v1",  # LM Studio Instance 2 (different port)
    api_key="not-needed",
    model_info={"vision": False, "function_calling": True, "json_output": False, "family": "unknown"},
)

# Option B: LM Studio + Ollama (uncomment to use)
# CODER_MODEL_CLIENT = OpenAIChatCompletionClient(
#     model="qwen2.5:7b",
#     base_url="http://localhost:1234/v1",  # LM Studio
#     api_key="not-needed",
#     model_info={"vision": False, "function_calling": True, "json_output": False, "family": "unknown"},
# )
#
# REVIEWER_MODEL_CLIENT = OpenAIChatCompletionClient(
#     model="qwen2.5:7b",
#     base_url="http://localhost:11434/v1",  # Ollama
#     api_key="not-needed",
#     model_info={"vision": False, "function_calling": True, "json_output": False, "family": "unknown"},
# )

# Option C: Single model (both agents use same LM Studio instance)
# (Just use same base_url for both - works but less diverse responses)

# ============ AGENT DEFINITIONS ============

def create_coder_agent():
    """Coding specialist agent"""
    return AssistantAgent(
        name="Coder",
        description="Expert Python/Kotlin developer",
        model_client=CODER_MODEL_CLIENT,
        system_message="""You are a senior software engineer specializing in:
- Python and Kotlin development
- Android app development
- Clean, maintainable code
- Best practices and design patterns

When writing code:
1. Include clear comments
2. Follow language conventions
3. Handle errors properly
4. Write production-ready code
""",
    )

def create_reviewer_agent():
    """Code review specialist agent"""
    return AssistantAgent(
        name="Reviewer",
        description="Code review and quality expert",
        model_client=REVIEWER_MODEL_CLIENT,
        system_message="""You are a code review specialist with expertise in:
- Finding bugs and security issues
- Performance optimization
- Code quality and maintainability
- Testing strategies

When reviewing:
1. Be constructive and specific
2. Point out both good and bad
3. Suggest concrete improvements
4. Consider edge cases
""",
    )

def create_planner_agent():
    """Task planning agent"""
    return AssistantAgent(
        name="Planner",
        description="Breaks down tasks into steps",
        model_client=CODER_MODEL_CLIENT,  # Can use either model
        system_message="""You are a technical planner. Your job is to:
1. Understand the user's requirements
2. Break complex tasks into clear, actionable steps
3. Identify potential challenges
4. Suggest the right approach

Do NOT write code - just plan the approach.
""",
    )

# ============ MAIN EXECUTION ============

async def run_multi_agent():
    """Run the multi-agent collaboration system"""
    print("=" * 60)
    print("🤖 AutoGen Multi-Agent System")
    print("=" * 60)
    print("\n📋 Configuration:")
    print("   Coder Model:    http://localhost:1234 (LM Studio)")
    print("   Reviewer Model: http://localhost:1235 (LM Studio #2)")
    print("   Planner Model:  http://localhost:1234 (LM Studio)")
    print("\n⚙️  Make sure:")
    print("   ✓ LM Studio Instance 1 running on port 1234")
    print("   ✓ LM Studio Instance 2 running on port 1235 (if using 2 instances)")
    print("   ✓ Models loaded in both instances")
    print("\n" + "=" * 60)
    
    # Create agents
    planner = create_planner_agent()
    coder = create_coder_agent()
    reviewer = create_reviewer_agent()
    
    # Create team with round-robin conversation
    team = RoundRobinGroupChat(
        [planner, coder, reviewer],
        max_turns=6,  # Each agent gets 2 turns
    )
    
    while True:
        user_input = input("\n💬 Your task (or 'quit'): ").strip()
        if user_input.lower() in ["quit", "exit", "q"]:
            break
        
        if not user_input:
            continue
        
        print("\n🔄 Agents collaborating...\n")
        print("-" * 60)
        
        try:
            # Run the team
            stream = team.run_stream(task=user_input)
            async for message in stream:
                if hasattr(message, 'content') and message.content:
                    agent_name = getattr(message, 'source', 'Unknown')
                    print(f"\n👤 {agent_name}:")
                    print(f"   {message.content}")
                    print()
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("\nTroubleshooting:")
            print("   1. Check LM Studio servers are running")
            print("   2. Verify models are loaded")
            print("   3. Check ports (1234, 1235)")
        
        print("-" * 60)
        print("✅ Task complete!\n")

if __name__ == "__main__":
    try:
        asyncio.run(run_multi_agent())
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
