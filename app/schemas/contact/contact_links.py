from pydantic import BaseModel


# Input Model
class ContactLinksBase(BaseModel):
    icon: str
    title: str
    url: str
    
    
# Update Model
class ContactLinksUpdate(BaseModel):
    icon: str | None = None
    title: str | None = None
    url: str | None = None
    
    
# Response Model
class ContactLinksResponse(BaseModel):
    id: int
    icon: str
    title: str
    url: str
    
    
    model_config = {
        "from_attributes": True
    }