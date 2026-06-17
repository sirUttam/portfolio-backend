from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.about import About, AboutCard
from app.schemas.about import AboutModel
from app.auth.dependencies import get_current_user

router = APIRouter()

@router.get('/about')
def get_about(db: Session = Depends(get_db)):
    
    about = db.query(About).first()

    if not about:
        return {
            "about_title": "",
            "subtitle": "",
            "image_url": "",
            "image_text": "",
            "cards": {
                "title": "",
                "description":""
            }
        }
    
    return about


@router.put('/about')
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
        db.refresh(new_card)
        
        return about
        
    # UPDATE existing about
    about.about_title = data.about_title
    about.subtitle = data.subtitle
    about.image_url = data.image_url
    about.image_text = data.image_text
    
    # Updating Cards Pending --------------------------------------------------------------------------------------------------
    
    db.commit()
    db.refresh(about)
    
    return about