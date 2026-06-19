from pydantic import BaseModel

# Input schema
class JourneyBase(BaseModel):
    title: str
    subtitle: str
    
    
# Update schema
class JourneyUpdate(BaseModel):
    title: str | None = None
    subtitle: str | None = None
    
    
# Response schema
class JourneyResponse(BaseModel):
    id: int
    title: str
    subtitle: str
    
    model_config = {
        "from_attributes": True
    }