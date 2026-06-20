from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.dependencies import get_current_user
from app.schemas.footer import FooterBase, FooterResponse, FooterUpdate
from app.models.footer import Footer

router = APIRouter()

@router.get("/footer", response_model=FooterResponse)
def get_hero(db: Session = Depends(get_db)):
    
    footer = db.query(Footer).first()
    
    if not footer:
       raise HTTPException(
           status_code=404, detail="Footer not found"
       )
    
    return footer



@router.put('/footer', response_model=FooterResponse)
def update_home(data:FooterUpdate, current_user: dict = Depends(get_current_user), db:Session = Depends(get_db)):
    
    footer = db.query(Footer).first()

    if not footer:
       raise HTTPException(
           status_code=404, detail="Footer not found"
       )
       
    updated_footer = data.model_dump(exclude_unset=True)
    for key, value in updated_footer.items():
        setattr(footer, key, value)
        
    db.commit()
    db.refresh(footer)

    return footer