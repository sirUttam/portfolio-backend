from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.about import About, AboutCard
from app.schemas.about import AboutModel, AboutResponse
from app.auth.dependencies import get_current_user

router = APIRouter()


from app.database import engine
from sqlalchemy import text

@router.get("/db-check")
def db_check():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        return {"db": "connected", "result": result.scalar()}
    
    
    

@router.get('/about', response_model=AboutResponse)
def get_about(db: Session = Depends(get_db)):
    
    about = db.query(About).first()

    if not about:
        raise HTTPException(
            status_code=404, detail="About not found"
        )
    
    return about


@router.put('/about', response_model=AboutResponse)
def update_about(data:AboutModel, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    
    about = db.query(About).first()

    # Create if not exist
    if not about:
        about = About(
            about_title = data.about_title,
            subtitle = data.subtitle,
            image_url = data.image_url,
            image_text = data.image_text,
        )
        db.add(about)
        db.commit()
        db.refresh(about)
        
        # Create cards
        for card in data.cards:
            new_card = AboutCard(
                title = card.title,
                description = card.description,
                about_id = about.id
            )
            db.add(new_card)
            
        db.commit()
        db.refresh(about)        
        return about
        
    # UPDATE existing about
    about.about_title = data.about_title
    about.subtitle = data.subtitle
    about.image_url = data.image_url
    about.image_text = data.image_text
    
    # Update existing cards
    for card_data in data.cards:
        card = db.query(AboutCard).filter(AboutCard.id == card_data.id).first()
        
        if card:
            card.title = card_data.title
            card.description = card_data.description
            
        
    db.commit()
    db.refresh(about)
    
    return about