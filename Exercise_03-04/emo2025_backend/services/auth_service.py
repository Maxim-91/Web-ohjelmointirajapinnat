from typing import Annotated

import bcrypt
import jwt
from fastapi import Depends

import models
from repos.auth_repo import AuthRepo, init_auth_repo


class AuthServ:
    def __init__(self, repo: AuthRepo):
        self.repo = repo

    def get_account(self, _auth, use_header=False):
        try:
            if use_header:
                _bearer, auth_token = _auth.split(' ')

                if _bearer != 'Bearer':
                    raise Exception('Invalid Bearer token')
            else:
                auth_token = _auth


            payload = jwt.decode(auth_token, verify=True, algorithms=['HS256'], key='secret')
            return self.repo.get_account(payload.get('id'))
        except Exception as e:
            raise e

    def login(self, username, password):
        user = self.repo.login(username, password)
        token_str = jwt.encode({'id': user.id}, key='secret', algorithm='HS256')
        return token_str

    def register(self, username, password):
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = models.User(username=username, password=hashed, role='user')
        self.repo.register(user)
        return user


def init_auth_service(repo: AuthRepo = Depends(init_auth_repo)):
    return AuthServ(repo)


AuthService = Annotated[AuthServ, Depends(init_auth_service)]
