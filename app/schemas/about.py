from pydantic import BaseModel


# Model for About cards
class AboutCardsModel(BaseModel):
    title: str
    description: str
    
    
    
# Model for about section
class AboutModel(BaseModel):
    about_title: str
    subtitle: str
    image_url: str
    image_text: str
    cards: list[AboutCardsModel]