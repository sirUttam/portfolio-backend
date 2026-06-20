from pydantic import BaseModel



class NavbarUpdate(BaseModel):
    logo_url: str | None = None
    site_name: str | None = None