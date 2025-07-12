#main.py

from fastapi import FastAPI,Depends
from app.requestModel import FetchUser
from psycopg2.extensions import connection
 
app = FastAPI(title="CRUD Operation", description="Crud Actions")

#Function root
@app.post("/")
async def root():
    return {"message": "FastAPI + PostgreSQL with dependency injection"}

#Function to fetchUser
@app.post("/v1/fetchUsers", summary="Function to fetch Users",
          description="Function to Fetch Users", tags =["Crud Operations"])
async def fetchUsers(request:FetchUser):
    resultStatus="success"
    message=""
    data={}
    try:
        data = f"Hi {request.username}"
        return {"status":resultStatus, "message":message, "data":data}
        
    except Exception as e:
        resultStatus ="error"
        message = f"Error in fetch Users function: {e}"
        return {"status":resultStatus, "message":message, "data":data}
        