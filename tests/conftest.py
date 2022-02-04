import random
import string
import time
from multiprocessing import Process

import pytest
import uvicorn

from app.database import data
from app.main import app


def run_server():
    uvicorn.run(app)


@pytest.fixture(scope="module")
def host():
    return "127.0.0.1:8000"


@pytest.fixture(scope="module")
def credentials():
    random_string = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))

    email = f"unitest_{random_string}@foo.com"
    return {"email": email, "password": "password"}


@pytest.fixture(scope="module")
def server(credentials):
    proc = Process(target=run_server, args=(), daemon=True)
    proc.start()
    time.sleep(2)
    yield

    conn = data.engine
    query = data.users.select().where(data.users.c.email == credentials["email"])
    user_result = next(conn.execute(query))

    query = data.blog.delete().where(data.blog.c.owner_id == user_result["id"])
    conn.execute(query)

    query = data.users.delete().where(data.users.c.email == credentials["email"])
    conn.execute(query)
    proc.kill()
