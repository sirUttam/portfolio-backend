from pydantic import BaseModel

class HeroBase(BaseModel):
    title: str | None=None
    subtitle: str | None=None
    description: str | None=None