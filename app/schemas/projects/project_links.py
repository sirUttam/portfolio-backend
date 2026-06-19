from pydantic import BaseModel


# Input Model
class ProjectLinksBase(BaseModel):
    type: str
    url: str
    
    
# Update Model
class ProjectLinksUpdate(BaseModel):
    type: str | None = None
    url: str  | None = None
    
    
# Response Model
class ProjectLinksResponse(BaseModel):
    id: int
    type: str
    url: str
    
    model_config = {
        "from_attributes": True
    }
