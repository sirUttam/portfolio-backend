from app.auth.dependencies import get_current_user
from fastapi import Depends, HTTPException, APIRouter, Response
from app.schemas.skills import ItemsResponse, ItemsBase, ItemsUpdate
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.skills.categories import SkillsCategory
from app.models.skills.items import SkillsItems



router = APIRouter()


    
# CRUD for Skills Items -------------------------------------------------------------------------------
# GET not needed as items will be shown throught GET/skills/categories

    
@router.post('/skills/items', response_model= ItemsResponse)
def create_item(data: ItemsBase, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    
    category = db.query(SkillsCategory).filter(SkillsCategory.id == data.category_id).first()

    if not category:
        raise HTTPException(
            status_code=404, detail="Category not found"
        )
    
    new_item = SkillsItems(
        icon = data.icon,
        title = data.title,
        category_id = data.category_id
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item


@router.put('/skills/items/{item_id}', response_model=ItemsResponse)
def update_item(data: ItemsUpdate, item_id: int, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    
    item = db.query(SkillsItems).filter(SkillsItems.id == item_id).first()

    if not item:
        raise HTTPException(
            status_code=404, detail="Item not found"
        )
    # if data.icon is not None:
    #     item.icon = data.icon
        
    # if data.title is not None:
    #     item.title = data.title
        
    # if data.category_id is not None:
    #     item.category_id = data.category_id
    
    updated_data = data.model_dump(exclude_unset=True)
    
    for key, value in updated_data.items():
        setattr(item, key, value)
    
    db.commit()
    db.refresh(item)

    return item


@router.delete('/skills/items/{item_id}')
def delete_item(item_id: int, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    
    item = db.query(SkillsItems).filter(SkillsItems.id == item_id).first()

    if not item:
        raise HTTPException(
            status_code=404, detail="Item not found"
        )

    db.delete(item)
    db.commit()

    return Response(status_code=204)
