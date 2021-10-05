from ariadne import SubscriptionType, convert_kwargs_to_snake_case
from graphql.type import GraphQLResolveInfo

from core import rabbit
from schemas import security
from schemas.error import MyGraphQLError

subscription = SubscriptionType()


@convert_kwargs_to_snake_case
@subscription.field("reviewblog")
async def review_blog_resolver(review_blog, info: GraphQLResolveInfo, token: str):
    return {"id": review_blog}


@convert_kwargs_to_snake_case
@subscription.source("reviewblog")
async def review_blog_source(obj, info: GraphQLResolveInfo, token: str):
    user = await security.get_current_user_by_auth_header(token)
    if not user:
        raise MyGraphQLError(code=401, message="User not authenticated")

    while True:
        blog_id = await rabbit.consumeblog()
        if blog_id:
            yield blog_id
        else:
            return
