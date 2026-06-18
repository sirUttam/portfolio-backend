from app.auth.dependencies import get_current_user
from fastapi import Depends, HTTPException, APIRouter
from app.schemas.skills import CategoryResponse, CategoryBase, ItemsResponse, ItemsBase
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.skills import SkillsCategory, SkillsItems


router = APIRouter()


# CRUD for Skills Category --------------------------------------------------------

@router.get('/skills/categories', response_model=list[CategoryResponse])
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

    
# CRUD for Skills Items --------------------------------------------------------
@router.get('/skills/{category_id}', response_model= list[ItemsResponse])
def get_items(category_id: int, db:Session = Depends(get_db)):
    
    items = db.query(SkillsItems).filter(SkillsItems.category_id == category_id).all()
    
    if not items:
        raise HTTPException(
            status_code=404, detail="Items not available"
        )
        
    return items

    
@router.post('/skills/{category_id}', response_model= ItemsResponse)
def create_item(data: ItemsBase, category_id: int, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    
    category = db.query(SkillsCategory).filter(SkillsCategory.id == category_id).first()

    if not category:
        raise HTTPException(
            status_code=404, detail="Category not found"
        )
    
    new_item = SkillsItems(
        icon = data.icon,
        title = data.title,
        category_id = category.id
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item


@router.put('/skills/{category_id}', response_model=ItemsResponse)
def update_item(data: ItemsBase, category_id: int, item_id: int, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    
    category = db.query(SkillsCategory).filter(SkillsCategory.id == category_id).first()

    if not category:
        raise HTTPException(
            status_code=404, detail="Category not found"
        )

    item = db.query(SkillsItems).filter(SkillsItems.id == item_id).first()

    if not item:
        raise HTTPException(
            status_code=404, detail="Item not found"
        )
    
    item.icon = data.icon
    item.title = data.title
    
    db.commit()
    db.refresh(item)

    return item
