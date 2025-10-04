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
        