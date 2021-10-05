import json

import httpx
import pytest

my_storage = {}


@pytest.fixture
def storage():
    return my_storage


@pytest.mark.asyncio
async def test_create_user(host, credentials, storage):
    query = """
        mutation createUser($email: String!, $password: String!) {
            createUser(email: $email, password: $password) {
                id,
                errors
            }
        }
    """

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"http://{host}/",
            timeout=60,
            json={"query": query, "variables": credentials},
        )
        json_response = json.loads(response.text)
        assert ("errors" in json_response) == False
        assert json_response["data"]["createUser"]["id"] is not None
        storage["user_id"] = json_response["data"]["createUser"]["id"]


@pytest.mark.asyncio
async def test_auth_user(host, credentials, storage):
    query = """
    mutation authUser($email: String!, $password: String!) {
        createToken(email: $email, password: $password) {
		    errors,
            token
        }
    }
    """

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"http://{host}/",
            headers={},
            timeout=60,
            json={"query": query, "variables": credentials},
        )
        json_response = json.loads(response.text)
        assert ("errors" in json_response) == False
        assert json_response["data"]["createToken"]["token"] is not None
        storage["token"] = json_response["data"]["createToken"]["token"]


async def create_blog(host, storage):
    query = """
    mutation createblog($title: String!, $description: String!) {
        createblog(title: $title, description: $description) {
		    errors
            id
        }
    }
    """
    token = storage["token"]

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"http://{host}/",
            headers={"Authorization": f"Bearer {token}"},
            timeout=60,
            json={
                "query": query,
                "variables": {"title": "title", "description": "description"},
            },
        )
        json_response = json.loads(response.text)
        assert ("errors" in json_response) == False
        assert json_response["data"]["createblog"]["id"] is not None


@pytest.mark.asyncio
async def test_create_blog(server, host, storage):
    await create_blog(host, storage)
