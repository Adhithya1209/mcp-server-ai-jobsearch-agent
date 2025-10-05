from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import json
load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant", api_key=os.getenv("GROQ_API_KEY"))



class mcp_server:
    def __init__(self, mcp_server_config: str="mcp.json"):
        self.llm = llm
        self.mcp_server_config = self.get_mcp_server_config(mcp_server_config)


    def get_mcp_server_config(mcp_server_config: str):
        with open(mcp_server_config, "r") as f:
            mcp_server_config = json.load(f)
        return mcp_server_config["mcpServers"]

    def get_llm(self):
        return self.llm
        
    def connect_to_mcp_server(self, mcp_server_config: str):
        mcp_server_config = self.get_mcp_server_config(mcp_server_config)
        return mcp_server_config["mcpServers"]
    

class agent_architecture:
    def __init__(self, mcp_server_config: str, system_prompt: str, user_prompt: str, llm: ChatGroq, agent_parameters: dict):
        self.mcp_server_config = mcp_server_config
        
        self.user_prompt = user_prompt
        self.parameters = agent_parameters
        self.llm = llm
        if isinstance(system_prompt, type(None)):
            self.system_prompt = "You are a helpful assistant. Be concise and friendly."
       
        else:
                self.system_prompt = system_prompt

    def conversation_history(self):
        conversation_history = [{"role": "system", "content": self.system_prompt}]
        conversation_history.append({"role": "system", "content": self.system_prompt})
        conversation_history.append({"role": "user", "content": self.user_prompt})
        return conversation_history

    def response(self):
        response = self.llm.chat.completions.create(
            model=self.model,
            messages=self.conversation_history(),
            **self.parameters
        )
        return response.choices[0].message.content
    
    def define_tools(self):
        tool_definitions = [
        {
            "type": "function",
            "function": {
                "name": "search_jobs",
                "description": "Search for job listings based on search term and location. Returns job postings with details like title, company, location, and description.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "search_term": {
                            "type": "string",
                            "description": "Job title or keywords to search for, e.g. 'Python Developer', 'Data Scientist'"
                        },
                        "location": {
                            "type": "string",
                            "description": "Location to search jobs in, e.g. 'San Francisco, CA', 'Remote'"
                        },
                        "results_wanted": {
                            "type": "integer",
                            "description": "Number of job results to return (default: 10)",
                            "default": 10
                        }
                    },
                    "required": ["search_term", "location"]
                }
            }
        }
    ]
        def search_jobs(self, search_term: str, location: str, results_wanted: int):
            mock_results = f"""
            Found {results_wanted} jobs for '{search_term}' in '{location}':
            
            1. Senior {search_term} - TechCorp
            Location: {location}
            Salary: $120k-150k
            Posted: 2 days ago
            
            2. {search_term} - StartupXYZ
            Location: {location}
            Salary: $100k-130k
            Posted: 5 days ago
            
            3. Lead {search_term} - BigCompany
            Location: {location}
            Salary: $140k-180k
            Posted: 1 week ago
            """
            
            return mock_results
        
        # Map function names to implementations
        available_functions = {
            "search_jobs": search_jobs
        }
        
        return tool_definitions, available_functions
            
    