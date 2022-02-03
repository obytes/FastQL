import sys
import traceback
from datetime import datetime, timedelta
from typing import Any, Dict, Optional, Union

from fastapi import security
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core import crud
from app.database.config import settings
from app.schemas.error import MyGraphQLError

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            seconds=settings.ACCESS_TOKEN_EXPIRE_SECONDS
        )
    to_encode = {
        "exp": expire.timestamp(),
        "sub": str(subject),
        "iat": datetime.utcnow(),
    }
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> Optional[int]:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError as e:
        traceback.print_exception(*sys.exc_info())
        raise MyGraphQLError(code=404, message="Invalid Token format")

    date_time_obj = datetime.fromtimestamp(payload["exp"])
    if date_time_obj < datetime.utcnow():
        raise MyGraphQLError(code=404, message="Token expired")

    return int(payload["sub"])


async def get_current_user_by_info(info) -> Optional[Dict]:
    auth_header = [
        blog[1]
        for blog in info.context["request"]["headers"]
        if blog[0] == b"authorization"
    ]
    if not auth_header:
        raise MyGraphQLError(code=404, message="Could not find Authorization header")

    return await get_current_user_by_auth_header(auth_header[0].decode())


async def get_current_user_by_auth_header(auth_header) -> Optional[Dict]:
    _, token = security.utils.get_authorization_scheme_param(auth_header)
    user_id = decode_access_token(token)

    return await crud.get_user_by_id(user_id=user_id)
