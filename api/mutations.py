import datetime

from ariadne import MutationType, convert_kwargs_to_snake_case

from core import crud, rabbit
from database import config, data
from schemas import security
from schemas.error import MyGraphQLError


@convert_kwargs_to_snake_case
async def resolve_create_blog(obj, info, title, description):
    user = await security.get_current_user_by_info(info)
    if not user:
        raise MyGraphQLError(code=401, message="User not authenticated")
    blog_id = await crud.create_blog(
        title=title, description=description, owner_id=user["id"]
    )

    await rabbit.produceblog(blog_id=blog_id)

    return {"id": blog_id}


@convert_kwargs_to_snake_case
async def resolve_create_user(obj, info, email, password):
    hashed_password = security.get_password_hash(password)
    params = {"email": email, "hashed_password": hashed_password}
    query = data.users.insert()
    result = await data.database.execute(query=query, values=params)

    return {"id": result}


@convert_kwargs_to_snake_case
async def resolve_login(obj, info, email, password):
    fetched_user = await crud.get_user_by_email(email=email)
    if not fetched_user:
        raise MyGraphQLError(code=404, message="Email not found")

    hashed_password = fetched_user["hashed_password"]
    is_authenticated = security.verify_password(password, hashed_password)

    if not is_authenticated:
        raise MyGraphQLError(code=401, message="Invalid password")

    access_token_expires = datetime.timedelta(
        seconds=config.settings.ACCESS_TOKEN_EXPIRE_SECONDS
    )
    token = security.create_access_token(
        fetched_user["id"], expires_delta=access_token_expires
    )
    return {"token": token}


mutation = MutationType()
mutation.set_field("createblog", resolve_create_blog)
mutation.set_field("createUser", resolve_create_user)
mutation.set_field("createToken", resolve_login)
