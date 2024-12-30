# AgenticAI
## Multi-Agent AI Framework for Web Search and Financial Insights

This project demonstrates the implementation of a multi-agent AI framework designed to perform web searches and provide financial data insights. The agents leverage advanced AI models and specialized tools for retrieving and summarizing data effectively.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### Overview
This project creates three AI agents:

- Web Search Agent: Performs web searches and retrieves information using DuckDuckGo, ensuring sources are included in the responses.
- Finance Agent: Fetches and summarizes financial data, such as stock prices, analyst recommendations, fundamentals, and company news using YFinanceTools.
- Multi-AI Agent: Combines the functionalities of the Web Search Agent and Finance Agent to provide comprehensive responses.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Requirements
- Python 3.8+
- phi library
- python-dotenv
- Environment variables for API keys
- Internet connection for web searches and financial data retrieval
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Environment Variables
Ensure you set the following environment variables in a .env file in the project directory:

- GROQ_API_KEY: API key for Groq model access.
- PHI_API_KEY: API key for Phi framework tools.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Code Breakdown
### Libraries and Imports
- phi: Provides tools and agent functionalities.
- dotenv: Manages environment variables.
- os: Accesses environment variables from the system.

## Agents
### Web Search Agent:
- Uses Groq’s llama3-groq-70b-8192-tool-use-preview model.
- Incorporates DuckDuckGo for web search.

### Finance Agent:
- Utilizes Groq’s llama3-groq-70b-8192-tool-use-preview model.
- Accesses financial data via YFinanceTools.

### Multi-AI Agent:
- Combines the above agents for a unified interface.

### Response Generation
- The multi_ai_agent.print_response() method processes a query and streams the result.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
