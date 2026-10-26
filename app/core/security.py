from passlib.context import CryptContext
import jwt
from app.core.config import settings
from fastapi.security  import OAuth2PasswordBearer
from fastapi import Depends
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from fastapi import HTTPException
from app.models.user import User
from sqlalchemy import select
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password : str , hashsed_password : str ):
    return pwd_context.verify(plain_password,hashsed_password)

def create_acess_token(data :dict)->str :
    to_encode = data.copy()
    token = jwt.encode(to_encode, settings.secret_key, settings.algorithm)
    return token
# the hashing part that is the bcrpt part verifes the authentication i.e who u are 
# then the jwt comes in and makes sure that u are allowed to do something 


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try :
        dtoken = jwt.decode(token,settings.secret_key,algorithms=[settings.algorithm])
        sub = dtoken["sub"]
        if not sub :
            raise HTTPException(status_code=401)
        q = select(User).where(
            User.id == sub
        )
        user = db.execute(q).scalar_one_or_none()

        if not user:
            raise HTTPException(status_code=401)
        return user 
    except:
        raise HTTPException(status_code=401)
    