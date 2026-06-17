from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends
from app.auth.jwt_handler import verify_token



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
