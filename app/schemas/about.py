from pydantic import BaseModel


# Input Models

# Model for About cards
class AboutCardsModel(BaseModel):
    id: int
    title: str
    description: str
    
    
    
# Model for about section
class AboutModel(BaseModel):
    about_title: str
    subtitle: str
    image_url: str
    image_text: str
    cards: list[AboutCardsModel]
    

# Card Response Model
class AboutCardResponse(BaseModel):
    id: int
    title: str
    description: str
    
    model_config={
        "from_attributes":True
    }


# About Response Model
class AboutResponse(BaseModel):
    id: int
    about_title: str
    subtitle: str
    image_url: str
    image_text: str
    
    cards: list[AboutCardResponse]
    
    model_config={
        "from_attributes": True
    }
    
    
