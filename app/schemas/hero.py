from pydantic import BaseModel


# Input Model
class HeroBase(BaseModel):
    title: str | None=None
    subtitle: str | None=None
    description: str | None=None
    
    
# Response Model
class HeroResponse(BaseModel):
    id: int
    title: str
    subtitle: str
    description: str
    
    model_config = {
        "from_attributes": True
    }