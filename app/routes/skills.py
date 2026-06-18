from app.auth.dependencies import get_current_user
from fastapi import Depends, HTTPException, APIRouter
from app.schemas.skills import CategoryResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.skills import SkillsCategory, SkillsItems


router = APIRouter()

@router.get('/skills', response_model=CategoryResponse)
def get_skills(db:Session = Depends(get_db)):
    
    skills = db.query(SkillsCategory).first()

    if not skills:
        raise HTTPException(
            status_code=404, detail="Skills not available"
        )
        
    return skills



    