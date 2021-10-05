import databases
import sqlalchemy as db

from database.config import settings

database = databases.Database(
    settings.SQLALCHEMY_DATABASE_URI,
    ssl=settings.SQLALCHEMY_DATABASE_SSL,
    min_size=settings.SQLALCHEMY_DATABASE_MIN_POOL,
    max_size=settings.SQLALCHEMY_DATABASE_MAX_POOL,
)

metadata = db.MetaData()

users = db.Table(
    "users",
    metadata,
    db.Column("id", db.Integer, primary_key=True),
    db.Column("email", db.String, nullable=False),
    db.Column("hashed_password", db.String, nullable=False),
    db.Column("created_date", db.DateTime),
)

blog = db.Table(
    "blog",
    metadata,
    db.Column("id", db.Integer, primary_key=True),
    db.Column("title", db.String, nullable=False),
    db.Column("description", db.String, nullable=True),
    db.Column("owner_id", db.Integer, nullable=False),
    db.Column("created_date", db.DateTime),
)

engine = db.create_engine(settings.SQLALCHEMY_DATABASE_URI, connect_args={}, echo=True)
metadata.create_all(engine)
