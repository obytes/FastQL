from typing import Dict, Optional

from database.data import blog, database, users
from schemas.error import MyGraphQLError


async def get_user_by_email(email: str) -> Optional[Dict]:
    query = users.select().where(users.c.email == email)
    user = await database.fetch_one(query=query)
    return dict(user) if user else None


async def get_user_by_id(user_id: int) -> Optional[Dict]:
    query = users.select().where(users.c.id == user_id)
    user = await database.fetch_one(query=query)
    return dict(user) if user else None


async def get_blogs(
    skip: Optional[int] = 0, limit: Optional[int] = 100
) -> Optional[Dict]:
    query = blog.select(offset=skip, limit=limit)
    result = await database.fetch_all(query=query)
    return [dict(blog) for blog in result] if result else None


async def get_blog(blog_id: int) -> Optional[Dict]:
    query = blog.select().where(blog.c.id == int(blog_id))
    result = await database.fetch_one(query=query)
    return dict(result) if result else None


async def create_user(email: str, hashed_password: str) -> int:
    fetched_user = await get_user_by_email(email)
    if fetched_user:
        raise MyGraphQLError(code=409, message="Email already registered")

    params = {"email": email, "hashed_password": hashed_password}
    query = users.insert()
    user_id = await database.execute(query=query, values=params)
    return user_id


async def create_blog(title: str, description: str, owner_id: str) -> int:
    params = {"title": title, "description": description, "owner_id": owner_id}
    query = blog.insert()
    blog_id = await database.execute(query=query, values=params)
    return blog_id
