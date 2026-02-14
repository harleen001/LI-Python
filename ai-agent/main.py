import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict
from langchain_groq import ChatGroq
from langchain.agents import create_agent 
from tools import execute_sql, create_local_file

load_dotenv()
app = FastAPI()

class UserRequest(BaseModel):
    model_config = ConfigDict(protected_namespaces=())
    prompt: str

llm = ChatGroq(
    model="llama-3.3-70b-versatile", 
    temperature=0, 
    #groq_api_keydemooooooooooo=os.getenv("demoapi")
)

tools = [execute_sql, create_local_file]

agent = create_agent(
    llm, 
    tools=tools, 
    system_prompt=(
        "You are a technical executor. When a user provides a script or a file request, "
        "execute the tool immediately. Once a tool returns 'SUCCESS', your job is done. "
        "Do not explain your steps or ask for more info."
    )
)

@app.post("/run")
async def handle_request(request: UserRequest):
    try:
        # Lower limit (5) ensures the agent doesn't loop more than once
        config = {"recursion_limit": 5} 
        result = agent.invoke({"input": request.prompt}, config=config)
        
        if "output" in result:
            return {"output": result["output"]}
        return {"output": result["messages"][-1].content}
            
    except Exception as e:
        return {"error": f"Task Interrupted: {str(e)}"}

if __name__ == "__main__":
    # CRITICAL: reload_excludes prevents the server from restarting when hello.py is created
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True,
        reload_excludes=["*.py", "*.txt", "*.log"] 
    )