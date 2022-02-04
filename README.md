# FastQL - FastAPI GraphQL Playground 🔧

![fastql](.github/header.svg)

<p align="center">
    <em>Generate a FullStack playground using FastAPI and GraphQL and Ariadne ⚡</em>
</p>

This Repository is based on this Article [Getting started with GraphQL in Python with FastAPI and Ariadne](https://www.obytes.com/blog/getting-started-with-graphql-in-python-with-fastapi-and-ariadne), Read Article to know how to use it.

## Overview 📌

- FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- GraphQL used to create a schema to describe all the possible data that clients can query through that service. A GraphQL schema is made up of object types, which define which kind of object you can request and what fields it has.
- Ariadne is a Python library for implementing GraphQL servers using schema-first approach.

## Features

- Full Docker integration (Docker based).
- Docker Compose integration and optimization for local development.
- Production ready Python web server using Uvicorn and Gunicorn.
- **GraphQL** playground based on Graphene and Ariadne.
- **Docker Compose** integration and optimization for local development.
- **Production ready** Python web server using Uvicorn.
- **Secure password** hashing by default.
- **JWT token** authentication.
- **SQLAlchemy** database integration using PostgreSQL.
- **Alembic** migrations for database schema.
- **rabbitMQ** (asynchronous) message broker.
- API tests based on **Pytest**, integrated with Docker, so you can test the full API interaction, independent on the database.

## Getting Started

### Project setup

```sh
# clone the repo
$ git clone https://github.com/obytes/fastql.git

# move to the project folder
$ cd fastql
```

## Running the Docker Container

- We have the Dockerfile created in above section. Now, we will use the Dockerfile to create the image of the FastAPI app and then start the FastAPI app container.
- Using a preconfigured `Makefile` tor run the Docker Compose:

```sh
# Pull the latest image
$ make pull

# Build the image
$ make build

# Run the container
$ make start
```

### Testing

While i use `HTTPX` an HTTP client for Python 3, to test the API, most of the tests are using a live log thats why need before to run a server using `uvicorn` and migrate the database, then you will have the ability to run the tests. To have a clean environment, recommended to use Docker for that, when you start the containers try to open the application container and then run `pytest` to test the API.

## License

This project is licensed under the terms of the MIT license.
