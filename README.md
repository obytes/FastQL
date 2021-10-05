![fastql](.github/header.svg)

# FastQL - FastAPI GraphQL Playground

Generate a FullStack playground using FastAPI and GraphQL and Ariadne :rocket:.

This Repository is based on this Article [Getting started with GraphQL in Python with FastAPI and Ariadne](https://www.obytes.com/blog/getting-started-with-graphql-in-python-with-fastapi-and-ariadne), Read Article to know how to use it.

## Overview

- FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- GraphQL used to create a schema to describe all the possible data that clients can query through that service. A GraphQL schema is made up of object types, which define which kind of object you can request and what fields it has.
- Ariadne is a Python library for implementing GraphQL servers using schema-first approach.

## Features

- Full **Docker** integration (Docker based).
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

### Prerequisites

- Python 3.8.6 or higher.
- Docker.

### Project setup

```sh
# clone the repo
$ git clone https://github.com/obytes/fastql.git

# move to the project folder
$ cd fastql
```

### Creating virtual environment

- Create a virtual environment using virtualenv.

```shell
# creating virtual environment
$ virtualenv venv

# activate virtual environment
$ source venv/bin/activate

# install all dependencies
$ pip install -r requirements.txt
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

__Note__: Running the test on the Container CLI `pytest` or when you use the command `make start` the container will be started and the tests will be run before the Uvicorn server is started.

### Environment variables

```sh
SECRET_KEY= #secret key for JWT token
QUEUE= #rabbitMQ queue name
```

> change all the environment variables in the `.env.example` and don't forget to rename it to `.env`.

## Preconfigured Packages

Includes preconfigured packages to kick start FastQL by just setting appropriate configuration.

| Package                                                      | Usage                                                            |
| ------------------------------------------------------------ | ---------------------------------------------------------------- |
| [FastAPI](https://fastapi.tiangolo.com/)                    | FastAPI is a modern, fast (high-performance), web framework for developing APIs with Python 3.6+ based on standard Python type hints. |
| [GraphQL](https://graphql.org/)                             | GraphQL used to create a schema to describe all the possible data that clients can query through that service. A GraphQL schema is made up of object types, which define which kind of object you can request and what fields it has. |
| [Ariadne](https://ariadnegraphql.org/)                       | Ariadne is a Python library for implementing GraphQL servers using schema-first approach. |

## Contributing

- If you have any questions or suggestions, please open an issue or create a pull request.
- If you are a contributor, please check out:
  - Is your pull request or issue relate with FastAPI?
  - Is your pull request or issue relate with GraphQL?
  - And make sure you take a look at the schema of the GraphQL playground. [schema.graphql](graphql/schema.graphql)
  - Also for People who gonna add a new features or fix somethings please make sure that its build on Docker.

## License

This project is licensed under the terms of the MIT license.