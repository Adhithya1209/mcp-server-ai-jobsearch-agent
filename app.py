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
    def __init__(self, mcp_server_config: str, system_prompt: str, user_prompt: str):
        self.mcp_server_config = mcp_server_config
        self.system_prompt = system_prompt
        self.user_prompt = user_prompt
        self.parameters = None


    def conversation_history(self):
        conversation_history = [{"role": "system", "content": self.system_prompt}]
        conversation_history.append({"role": "system", "content": self.system_prompt})
        conversation_history.append({"role": "user", "content": self.user_prompt})
        return conversation_history
    
  
    
        
    