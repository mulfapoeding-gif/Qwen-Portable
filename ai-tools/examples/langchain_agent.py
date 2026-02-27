"""
LangChain Agent with DuckDuckGo Search + LM Studio
===================================================
Example: AI agent with web search capabilities using local models
"""

from langchain_community.tools import DuckDuckGoSearchResults
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# Initialize DuckDuckGo search tool
search = DuckDuckGoSearchResults(max_results=5)

# Create LangChain tool from search
tools = [search]

# Create LLM with LM Studio (local model)
llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="not-needed",
    model="local-model",
    temperature=0.7,
)

# Simple research agent prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a research assistant with access to web search.
When the user asks about current events, technical topics, or needs information,
use the search tool to find relevant information.

Always cite your sources from search results.
If search results are not helpful, say so honestly.
"""),
    ("human", "{input}"),
])

# Create chain
chain = prompt | llm | StrOutputParser()

def search_query(query: str) -> str:
    """Run a search query and return formatted results"""
    try:
        results = search.run(query)
        return f"Search results for '{query}':\n{results}"
    except Exception as e:
        return f"Search failed: {e}"

if __name__ == "__main__":
    print("=== LangChain Research Agent ===")
    print("Make sure LM Studio server is running on http://localhost:1234")
    print()
    
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ["quit", "exit", "q"]:
            break
        
        # Check if we should search
        if any(word in user_input.lower() for word in ["search", "find", "look up", "research"]):
            print("\n🔍 Searching...")
            search_result = search_query(user_input)
            print(search_result)
        else:
            print("\n🤖 AI: ", end="")
            response = chain.invoke({"input": user_input})
            print(response)
