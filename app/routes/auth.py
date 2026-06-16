from fastapi import APIRouter, Depends, HTTPException
from app.schemas.hero import HeroBase
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.hero import Hero
from app.schemas.auth import LoginBase
from app.models.admin import Admin
from app.auth.utils import verify_password
from app.auth.jwt_handler import token_generation, verify_token
from fastapi.security import OAuth2PasswordBearer


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
    
# Now for protected routes we need to extract and verify the token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='admin')

# verify the current user
def get_current_user(token: str = Depends(oauth2_scheme)):
    
    payload = verify_token(token)
    
    if not payload:
        raise HTTPException(
            status_code=401, detail="Invalid token"
        )
    
    return payload



# Protected route ( Updating the hero section ) -----------------------------------

@router.put('/')
def update_home(data:HeroBase, current_user: dict = Depends(get_current_user), db:Session = Depends(get_db)):
    
    # 1. check if hero exists
    hero = db.query(Hero).filter(Hero.id == current_user['id']).first()

    # 2. if not exists → create
    if not hero:
        hero = Hero(
            title = data.title,
            subtitle = data.subtitle,
            description = data.description
        )
        db.add(hero)

    # 3. if exists → update
    else:
        if data.title is not None:
            hero.title = data.title
            
        if data.subtitle is not None:
            hero.subtitle = data.subtitle
            
        if data.description is not None:
            hero.description = data.description
        
        
    # 4. save changes
    db.commit()
    db.refresh(hero)
    
    return hero
    