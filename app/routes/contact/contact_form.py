from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.dependencies import get_current_user
from app.database import get_db
from app.schemas.contact.contact_form import ContactFormBase, ContactFormResponse
from app.models.contact.contact_form import ContactForm



router = APIRouter()


@router.get('/contact/messages', response_model=list[ContactFormResponse])
def get_form(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    
    messages = db.query(ContactForm).all()
    
    if not messages:
        raise HTTPException(
            status_code=404, detail="Messages not found"
        )
        
    return messages


@router.post('/contact/messages', response_model=ContactFormResponse)
def create_form(data: ContactFormBase, db: Session = Depends(get_db)):
    
    
    new_message = ContactForm(
        name = data.name,
        email = data.email,
        message = data.message
    )
    
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
        
    return new_message



@router.delete('/contact/messages/{form_id}')
def delete_form(form_id: int, current_user:dict = Depends(get_current_user), db: Session = Depends(get_db)):
    
    message = db.query(ContactForm).filter(ContactForm.id == form_id).first()

    if not message:
        raise HTTPException(
            status_code=404, detail="Message not found"
        )
    
    db.delete(message)
    db.commit()

    return {"message": "Deleted successfully"}