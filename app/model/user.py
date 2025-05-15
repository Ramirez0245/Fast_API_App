from pydantic import BaseModel

import jwt

class Type_User_Create(BaseModel):
    username: str
    password: str
    password_match: str

class Type_Login(BaseModel):
    username: str
    password: str    