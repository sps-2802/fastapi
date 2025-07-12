# requestModel.py
from pydantic import BaseModel,Field

class FetchUser(BaseModel):
    username:str|None