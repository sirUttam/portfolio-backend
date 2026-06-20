from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from app.auth.dependencies import get_current_user
from sqlalchemy.orm import Session
from app.models.navbar import SiteSettings
from app.schemas.navbar import NavbarUpdate, NavbarResponse


router = APIRouter()



@router.get("/settings/navbar", response_model=NavbarResponse)
def get_navbar(db: Session = Depends(get_db)):
    return db.query(SiteSettings).first()



@router.put("/settings/navbar", response_model=NavbarResponse)
def update_navbar(data: NavbarUpdate, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):

    settings = db.query(SiteSettings).first()

    if not settings:
        settings = SiteSettings()

    updated_data = data.model_dump(exclude_unset=True)

    for key, value in updated_data.items():
        setattr(settings, key, value)

    db.add(settings)
    db.commit()
    db.refresh(settings)

    return settings