import time
from typing import Dict

import jwt
from fastapi import APIRouter, Body, Depends, Header, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

from ohmyapi.builtin.auth.models import User

import settings

# Router
router = APIRouter(prefix="/auth", tags=["auth"])

# Secrets & config (should come from settings/env in real projects)
JWT_SECRET = getattr(settings, "JWT_SECRET", "changeme")
JWT_ALGORITHM = getattr(settings, "JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_SECONDS = getattr(settings, "JWT_ACCESS_TOKEN_EXPIRE_SECONDS", 15 * 60)
REFRESH_TOKEN_EXPIRE_SECONDS = getattr(settings, "JWT_REFRESH_TOKEN_EXPIRE_SECONDS", 7 * 24 * 60 * 60)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def create_token(data: dict, expires_in: int) -> str:
    to_encode = data.copy()
    to_encode.update({"exp": int(time.time()) + expires_in})
    token = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    if isinstance(token, bytes):
        token = token.decode("utf-8")
    return token


def decode_token(token: str) -> Dict:
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """Dependency: extract user from access token."""
    payload = decode_token(token)
    username = payload.get("sub")
    if username is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload")

    user = await User.filter(username=username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user


async def require_authenticated(current_user: User = Depends(get_current_user)) -> User:
    """Ensure the current user is an admin."""
    if not current_user:
        raise HTTPException(403, "Authentication required")
    return current_user


async def require_admin(current_user: User = Depends(get_current_user)) -> User:
    """Ensure the current user is an admin."""
    if not current_user.is_admin:
        raise HTTPException(403, "Admin privileges required")
    return current_user


async def require_staff(current_user: User = Depends(get_current_user)) -> User:
    """Ensure the current user is a staff member."""
    if not current_user.is_staff:
        raise HTTPException(403, "Staff privileges required")
    return current_user


async def require_group(
    group_name: str, 
    current_user: User = Depends(get_current_user)
) -> User:
    """Ensure the current user belongs to the given group."""
    user_groups = await current_user.groups.all()
    if not any(g.name == group_name for g in user_groups):
        raise HTTPException(
            status_code=403,
            detail=f"User must belong to group '{group_name}'"
        )
    return current_user


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/login")
async def login(form_data: LoginRequest = Body(...)):
    """Login with username & password, returns access and refresh tokens."""
    user = await User.authenticate(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = create_token({"sub": user.username, "type": "access"}, ACCESS_TOKEN_EXPIRE_SECONDS)
    refresh_token = create_token({"sub": user.username, "type": "refresh"}, REFRESH_TOKEN_EXPIRE_SECONDS)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


@router.post("/refresh")
async def refresh_token(refresh_token: str):
    """Exchange refresh token for new access token."""
    payload = decode_token(refresh_token)
    if payload.get("type") != "refresh":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

    username = payload.get("sub")
    user = await User.filter(username=username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    new_access = create_token({"sub": user.username, "type": "access"}, ACCESS_TOKEN_EXPIRE_SECONDS)
    return {"access_token": new_access, "token_type": "bearer"}


@router.get("/me")
async def me(current_user: User = Depends(get_current_user)):
    """Return the currently authenticated user."""
    return {
        "username": current_user.username,
        "is_admin": current_user.is_admin,
        "is_staff": current_user.is_staff,
    }
