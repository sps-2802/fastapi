#main.py

from fastapi import FastAPI,Depends
from requestModel import FetchUser
from db import getConnection
from psycopg2.extensions import connection
 
app = FastAPI(title="CRUD Operation", description="Crud Actions")

@app.post("/")
async def root():
    return {"message": "FastAPI + PostgreSQL with dependency injection"}

@app.post("/v1/fetchUsers", summary="Function to fetch Users",
          description="Function to Fetch Users", tags =["Crud Operations"])
async def fetchUsers(request:FetchUser,conn:connection=Depends(getConnection)):
    resultStatus="success"
    message=""
    data={}
    try:
        username=request.username.strip()
        cur = conn.cursor()
        fetchUsersSql = "SELECT * FROM users"
        if username:
            fetchUsersSql += f" where name='{username}'"
        cur.execute(fetchUsersSql)
        fetchUsersResult = cur.fetchmany()
        data=fetchUsersResult
        return {"status":resultStatus, "message":message, "data":data}
        
    except Exception as e:
        resultStatus ="error"
        message = f"Error in fetch Users function: {e}"
        return {"status":resultStatus, "message":message, "data":data}
        