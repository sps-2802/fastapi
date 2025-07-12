# requestModel.py
from pydantic import BaseModel

class FetchUser(BaseModel):
    username:str