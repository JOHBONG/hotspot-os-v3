from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from backend.app.models import User
from datetime import datetime, timedelta
import jwt

SECRET_KEY = "super-jwt-key"  # Use env var in production
ALGORITHM = "HS256"

router = APIRouter()

fake_users_db = {
    "admin": {
        "id": 1, "name": "Admin User", "phone": "+255711000111", "roles": ["admin"], "password": "admin", "last_login": None, "is_active": True
    }
}

class LoginForm(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if not user or user['password'] != password:
        return None
    return user

def create_access_token(data: dict, expires_delta=timedelta(hours=6)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode["exp"] = expire
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/auth/login", response_model=Token)
def login(form: LoginForm):
    user = authenticate_user(form.username, form.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token({"sub": user["name"], "roles": user["roles"]})
    user['last_login'] = datetime.utcnow().isoformat()
    return {"access_token": token, "token_type": "bearer"}
