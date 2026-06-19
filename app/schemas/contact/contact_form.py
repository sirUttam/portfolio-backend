from pydantic import BaseModel


# Input Model
class ContactFormBase(BaseModel):
    name: str
    email: str
    message: str
    
    
    
# Response Model
class ContactFormResponse(BaseModel):
    id: int
    name: str
    email: str
    message: str
    
    model_config = {
        "from_attributes": True
    }