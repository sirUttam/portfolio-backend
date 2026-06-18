from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from sqlalchemy.orm import Session
from app.models.hero import Hero
from app.schemas.hero import HeroBase, HeroResponse
from app.auth.dependencies import get_current_user

router = APIRouter()


@router.get("/", response_model=HeroResponse)
def get_hero(db: Session = Depends(get_db)):
    
    hero = db.query(Hero).first()
    
    if not hero:
       raise HTTPException(
           status_code=404, detail="Hero not found"
       )
    
    return hero



# Protected route ( Updating the hero section ) -----------------------------------

@router.put('/', response_model=HeroResponse)
def update_home(data:HeroBase, current_user: dict = Depends(get_current_user), db:Session = Depends(get_db)):
    
    # 1. check if hero exists
    hero = db.query(Hero).first()

    # 2. if not exists → create
    if not hero:
        hero = Hero(
            title = data.title,
            subtitle = data.subtitle,
            description = data.description
        )
        db.add(hero)

    # 3. if exists → update
    else:
        if data.title is not None:
            hero.title = data.title
            
        if data.subtitle is not None:
            hero.subtitle = data.subtitle
            
        if data.description is not None:
            hero.description = data.description
        
        
    # 4. save changes
    db.commit()
    db.refresh(hero)
    
    return hero