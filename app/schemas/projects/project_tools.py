from pydantic import BaseModel


# Input tool
class ProjectToolsBase(BaseModel):
    title: str
    
    
# Update tool 
class ProjectToolsUpdate(BaseModel):
    title: str | None = None
    
    
# Response tool
class ProjectToolsResponse(BaseModel):
    id: int
    title: str
    
    model_config = {
        "from_attributes": True
    }
