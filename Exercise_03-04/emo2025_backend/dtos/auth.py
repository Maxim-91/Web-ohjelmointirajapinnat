from pydantic import BaseModel


class LoginReq(BaseModel):
    username: str
    password: str

class AuthDto(BaseModel):
    id: int
    username:str
    role:str