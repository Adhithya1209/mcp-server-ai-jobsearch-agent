# mcp-server-ai-jobsearch-agent
Agent that searches for job postings in social media like linkedin and indeed

1) The project consists of a configuration file for the mcp servers with jobspy tool and others to do the search in social media networks
2) The app.py consists of mainly of a class to configure the mcp servers from the configuration file provided as json and a class to configure the user, system prompts for the llm
3) The llm model used here is llama-3.1-8b-instant using the api key provided from groq for fast compuatation using LPU. The api key is provided in a system level .env file. Therefore to use the model a api key should be provided in secrets and environmental variable.
