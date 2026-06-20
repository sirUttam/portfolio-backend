from pydantic import BaseModel


# Input Schema
class FooterBase(BaseModel):
    title: str
    subtitle: str
    copyright_text: str
    url: str
    
    
# Update Schema
class FooterUpdate(BaseModel):
    title: str | None = None
    subtitle: str | None = None
    copyright_text: str | None = None
    url: str | None = None
    
    


# Response Schema
class FooterResponse(BaseModel):
    id: int
    title: str
    subtitle: str
    copyright_text: str
    url: str
    
    model_config = {
        "from_attributes": True
    }