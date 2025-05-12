from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

engine = create_engine('sqlite:///emo_2025.sqlite?check_same_thread=False')
session = sessionmaker(bind=engine, autocommit=False, expire_on_commit=False)


def connect_to_db():
    conn = None
    try:
        conn = session()
        yield conn
    finally:
        if conn is not None:
            conn.close()
