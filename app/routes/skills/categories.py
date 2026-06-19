from app.auth.dependencies import get_current_user
from fastapi import Depends, HTTPException, APIRouter
from app.schemas.skills import CategoryResponse, CategoryBase
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.skills.categories import SkillsCategory

router = APIRouter()


# CRUD for Skills Category --------------------------------------------------------

@router.get('/skills', response_model=list[CategoryResponse])
def get_skills(db:Session = Depends(get_db)):
    
    skills = db.query(SkillsCategory).all()

    if not skills:
        raise HTTPException(
            status_code=404, detail="Skills not available"
        )
        
    return skills


@router.post('/skills/categories', response_model=CategoryResponse)
def create_categories(data: CategoryBase, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):

    new_category = SkillsCategory(
        title = data.title
    )
    
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    
    return new_category

@router.put('/skills/categories/{id}', response_model=CategoryResponse)
def update_categories(data: CategoryBase, id:int, current_user:dict = Depends(get_current_user), db: Session= Depends(get_db)):
    
    category = db.query(SkillsCategory).filter(SkillsCategory.id == id).first()

    if not category:
        raise HTTPException(
            status_code=404, detail="Category not found"
        )
        
    if data.title is not None:
        category.title = data.title
    
    db.commit()
    db.refresh(category)

    return category


@router.delete('/skills/categories/{id}')
def delete_category(id: int, db:Session = Depends(get_db)):
    
    category = db.query(SkillsCategory).filter(SkillsCategory.id == id).first()

    if not category:
        raise HTTPException(
            status_code=404, detail="Category not found"
        )
        
    db.delete(category)
    db.commit()

    return {
        "message": "Category deleted successfully"
    }