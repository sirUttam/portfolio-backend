from pydantic import BaseModel
from app.schemas.projects.project_links import ProjectLinksResponse
from app.schemas.projects.project_tools import ProjectToolsResponse



# Input Model
class ProjectBase(BaseModel):
    title: str
    description: str
    

# Update model
class ProjectUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    
    
# Response Model
class ProjectResponse(BaseModel):
    id: int
    title: str
    description: str
    
    tools: list[ProjectToolsResponse]
    links: list[ProjectLinksResponse]

    model_config = {
        "from_attributes": True
    }
    
