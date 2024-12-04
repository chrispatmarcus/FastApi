from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session

SQLALCHAMY_DATABASE_URL ='sqlite:///./blog.db'

engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={"check_same_thread":False})

SessionLocal = Session(bind=engine, autocommit=False, autoflush=False)

Base=DeclarativeBase
