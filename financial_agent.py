from phi.agent import Agent
from phi.tools.yfinance import YFinanceTools
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
phi_api_key = os.getenv("PHI_API_KEY")

# Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo(),],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

# Financial Agent
finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)
        ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

# Multi AI Agent which is combining both of them
multi_ai_agent=Agent(
    team=[web_search_agent, finance_agent],
    model=Groq(id="llama3-8b-8192"),
    instructions=["Always include sources","Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)


# multi_ai_agent.print_response("Summerize analyst recommendation and share the latest news for NVDA", stream=True)

# Attempt to generate a response
try:
    response = multi_ai_agent.print_response(
        "Summarize analyst recommendation and share the latest news for NVDA",
        stream=True
    )
    print(response)
except Exception as e:
    print("An error occurred:", e)