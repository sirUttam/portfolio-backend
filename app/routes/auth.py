from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.auth import LoginBase
from app.models.admin import Admin
from app.auth.utils import verify_password
from app.auth.jwt_handler import token_generation


router = APIRouter()


# Login route for admin
@router.post('/admin')
def login(data: LoginBase, db: Session = Depends(get_db)):
    
    email = db.query(Admin).filter(Admin.email == data.email).first()

    if not email:
        raise HTTPException(
            status_code=401, detail="Invalid username"
        )
    
    password = verify_password(data.password, email.password)
    
    if not password:
        raise HTTPException(
            status_code= 401, detail="Invalid password"
        )
    
    token = token_generation({"id":email.id, "email": email.email})
    
    return {
        "access_token": token,
        "token_type": "Bearer"
    }
    

    