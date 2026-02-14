import mysql.connector
import os
# --- ADD THIS IMPORT ---
from langchain_core.tools import tool 

@tool(return_direct=True)
def execute_sql(query: str):
    """Executes SQL commands. Once this runs, the task is finished."""
    print(f"--- AGENT EXECUTING SQL ---")
    try:
        conn = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST", "localhost"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            autocommit=True 
        )
        cursor = conn.cursor()
        
        # We iterate through the results generator to force MySQL to execute each line
        results = cursor.execute(query, multi=True)
        for result in results:
            if result.with_rows:
                result.fetchall()
                
        cursor.close()
        conn.close()
        return "SUCCESS: SQL commands physically committed to the database."
    except Exception as e:
        return f"SQL Error: {str(e)}"

@tool(return_direct=True)
def create_local_file(filename: str, code: str):
    """Creates a .py file. Call this to finish the task instantly."""
    print(f"--- AGENT CREATING FILE: {filename} ---")
    try:
        with open(filename, "w", encoding='utf-8') as f:
            f.write(code)
        return f"SUCCESS: {filename} was created in the project root."
    except Exception as e:
        return f"File Error: {str(e)}"