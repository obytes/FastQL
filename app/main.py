""" Generate a FullStack playground using FastAPI and GraphQL and Ariadne """

import uvicorn
from ariadne import (
    format_error,
    load_schema_from_path,
    make_executable_schema,
    snake_case_fallback_resolvers,
)
from ariadne.asgi import GraphQL
from fastapi import FastAPI
from graphql.error.graphql_error import GraphQLError

from app.api.mutations import mutation
from app.api.queries import query
from app.api.subscriptions import subscription
from app.database import data

app = FastAPI(
    title="FastQL",
    description="Generate a FullStack Application using GraphQL and FastAPI",
    version="1.0.0",
)


def my_format_error(error: GraphQLError, debug: bool = False) -> dict:
    if debug:
        return format_error(error, debug)

    formatted = error.formatted
    formatted["message"] = error.args[0]
    return formatted


@app.on_event("startup")
async def startup():
    await data.database.connect()


@app.on_event("shutdown")
async def shutdown():
    await data.database.disconnect()


type_defs = load_schema_from_path("graphql/schema.graphql")
resolvers = [query, mutation, subscription]
schema = make_executable_schema(type_defs, resolvers, snake_case_fallback_resolvers)

graphQL = GraphQL(schema, error_formatter=my_format_error, middleware=[], debug=False)


app.mount("/", graphQL)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, loop="asyncio")
