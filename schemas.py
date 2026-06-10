from pydantic import BaseModel,ConfigDict
from typing import Optional
from datetime import datetime
class User(BaseModel):
    email:str
    password:str
class Note(BaseModel):
    title:str
    content:str
class NoteResponse(BaseModel):
    id:int
    title:str
    content:str
    created_at:datetime
    model_config=ConfigDict(from_attributes=True)
class NoteUpdate(BaseModel):
    title:str
    