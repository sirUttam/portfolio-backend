from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.dependencies import get_current_user
from app.database import get_db
from app.schemas.contact.contact_links import ContactLinksBase, ContactLinksResponse, ContactLinksUpdate
from app.models.contact.contact_links import ContactLinks



router = APIRouter()



@router.get('/contact/links', response_model=list[ContactLinksResponse])
def get_contact_links(db: Session = Depends(get_db)):
    
    links = db.query(ContactLinks).all()

    if not links:
        raise HTTPException(
            status_code=404, detail="Links  not found"
        )
        
    return links



@router.post('/contact/links', response_model=ContactLinksResponse)
def create_contact_link(data: ContactLinksBase, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    
    
    new_link = ContactLinks(
        icon = data.icon,
        title = data.title,
        url = data.url
    )
    
    db.add(new_link)
    db.commit()
    db.refresh(new_link)
        
    return new_link



@router.put('/contact/links/{link_id}', response_model=ContactLinksResponse)
def update_contact_link(data: ContactLinksUpdate, link_id: int, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    
    link = db.query(ContactLinks).filter(ContactLinks.id == link_id).first()

    if not link:
        raise HTTPException(
            status_code=404, detail="Link  not found"
        )

    updated_link = data.model_dump(exclude_unset=True)

    for key, value in updated_link.items():
        setattr(link, key, value)
    
    db.commit()
    db.refresh(link)
    
    return link


@router.delete('/contact/links/{link_id}')
def delete_contact_link(link_id: int, current_user:dict = Depends(get_current_user), db: Session = Depends(get_db)):
    
    link = db.query(ContactLinks).filter(ContactLinks.id == link_id).first()

    if not link:
        raise HTTPException(
            status_code=404, detail="Link not found"
        )
    
    db.delete(link)
    db.commit()

    return {"message": "Deleted successfully"}