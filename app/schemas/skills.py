from pydantic import BaseModel


# Input model for skills items
class ItemsBase(BaseModel):
    icon: str
    title: str


# Input model for skills category
class CategoryBase(BaseModel):
    title: str
    items: list[ItemsBase]
    
    

# Response model for skills items
class ItemsResponse(BaseModel):
    id: int
    icon: str
    title: str
    
    model_config={
        "from_attributes": True
    }


# Response model for skills category
class CategoryResponse(BaseModel):
    id: int
    title: str
    items: list[ItemsResponse]
    
    model_config={
        "from_attributes": True
    }