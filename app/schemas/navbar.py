from pydantic import BaseModel



class NavbarUpdate(BaseModel):
    logo_url: str | None = None
    site_name: str | None = None
    
    
class NavbarResponse(BaseModel):
    id: int
    logo_url: str | None = None
    site_name: str

    model_config = {
        "from_attributes": True
    }