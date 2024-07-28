from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote_plus

USERNAME = 'postgres'
PASSWORD = 'xxxxx@'
HOST = '111.11.111.999'
PORT = '8989'
DATABASE = 'database'

encoded_password = quote_plus(PASSWORD)

SQLALCHEMY_DATABASE_URL = f'postgresql://{USERNAME}:{encoded_password}@{HOST}:{PORT}/{DATABASE}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()