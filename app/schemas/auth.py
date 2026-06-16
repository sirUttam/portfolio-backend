from pydantic import BaseModel

class LoginBase(BaseModel):
    email: str
    password: str