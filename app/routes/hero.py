from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from sqlalchemy.orm import Session
from app.models.hero import Hero
from app.schemas.hero import HeroBase

router = APIRouter()


@router.get("/")
def get_hero(db: Session = Depends(get_db)):
    
    hero = db.query(Hero).first()
    
    if not hero:
        return{
            "title": "",
            "subtitle": "",
            "description": ""
        }
    
    return hero
