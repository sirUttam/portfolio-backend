from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from app.auth.dependencies import get_current_user
from sqlalchemy.orm import Session
from app.models.navbar import SiteSettings
from app.schemas.navbar import NavbarUpdate


router = APIRouter()



@router.get("/settings/navbar")
def get_navbar(db: Session = Depends(get_db)):
    return db.query(SiteSettings).first()



@router.put("/settings/navbar")
def update_navbar(data: NavbarUpdate, db: Session = Depends(get_db)):

    settings = db.query(SiteSettings).first()

    if not settings:
        settings = SiteSettings()

    settings.logo_url = data.logo_url
    settings.site_name = data.site_name

    db.add(settings)
    db.commit()
    db.refresh(settings)

    return settings