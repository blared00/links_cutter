from decouple import config
import databases
import sqlalchemy
from sqlalchemy.orm import declarative_base

SQLALCHEMY_DATABASE_URL = (
         'postgresql://'
         + config('DB_USER')
         + ":"
         + config('DB_PASSWORD')
         + "@"
         + config('DB_HOST')
         + "/"
         + config('DB_NAME')
)


database = databases.Database(SQLALCHEMY_DATABASE_URL)

metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    SQLALCHEMY_DATABASE_URL
)
metadata.create_all(engine)

Base = declarative_base()
