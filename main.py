import random
import json
from fastmcp import FastMCP

mcp=FastMCP("Simple calculator server")

@mcp.tool
def add(a:int,b:int):
    "Add two numbers"
    return a+b

@mcp.tool
def random_number(min_val:int=1,max_val:int=100):
    "Generate random number"
    return random.randint(min_val,max_val)

@mcp.resource("info://server")
def server_info():
    "Get infoformation about this server"
    info={
        "name":"Simple Calculator server",
        "version":"1.0.0",
        "description":"A basic MCP server with math tools",
        "tools":["add","random_number"],
        "author":"Your Name"
    }
    return json.dumps(info,indent=2)

if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)
