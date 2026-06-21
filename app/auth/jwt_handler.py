from jose import jwt, JWTError
from datetime import datetime, timedelta,timezone
from fastapi import HTTPException
import os 
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


# For token generation using jwt

def token_generation(data: dict):
    
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=40)

    to_encode.update({'exp':expire})

    token_encoded = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    
    return token_encoded


# For token verify

def verify_token(token: str):
    
    try:
        payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )
        return payload
    
    except JWTError:
        raise HTTPException(
            status_code=401, detail="Invalid token"
        )