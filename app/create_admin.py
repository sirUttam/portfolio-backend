from app.models.admin import Admin
from app.database import SessionLocal
from app.auth.utils import hash_password

from dotenv import load_dotenv
import os

load_dotenv()


db = SessionLocal()

try:
    email = os.getenv("ADMIN_EMAIL")
    password = os.getenv("ADMIN_PASSWORD")
    
    admin_email = os.getenv("ADMIN_EMAIL")
    existing = db.query(Admin).filter(Admin.email == admin_email).first()

    if not existing:
        
         admin = Admin(
             email = email,
             password = hash_password(password)
         )

    db.add(admin)
    db.commit()
    
except Exception as e:
    db.rollback()
    print("Error:", e)

finally:
    db.close()