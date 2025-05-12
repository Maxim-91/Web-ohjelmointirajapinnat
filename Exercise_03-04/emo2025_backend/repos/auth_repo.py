import bcrypt
from fastapi import Depends
from sqlalchemy.orm import Session

import models
from custom_exceptions.custom_not_found import CustomNotFound
from db import connect_to_db


class AuthRepo  :
    def __init__(self, db: Session):
        self.db = db
    def login(self, username, password):
        user = self.db.query(models.User).filter(models.User.username == username).first()
        if not user:
            raise CustomNotFound('user not found1')
        password_bytes = password.encode('utf-8')
        correct = bcrypt.checkpw(password_bytes, user.password)
        if not correct:
            raise CustomNotFound('user not found2')
        return user


    def get_account(self, _id):
        user = self.db.query(models.User).filter(models.User.id == _id).first()
        if not user:
            raise CustomNotFound('user not found')
        return user

    def register(self, user):
        self.db.add(user)
        self.db.commit()



def init_auth_repo(db: Session = Depends(connect_to_db)):
    return AuthRepo(db)