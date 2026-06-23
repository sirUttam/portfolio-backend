from pydantic import BaseModel, EmailStr


# Input Model
class ContactFormBase(BaseModel):
    name: str
    email: EmailStr
    message: str
    
    
    
# Response Model
class ContactFormResponse(BaseModel):
    id: int
    name: str
    message: str
    
    model_config = {
        "from_attributes": True
    }