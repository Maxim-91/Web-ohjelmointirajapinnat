from fastapi import APIRouter, HTTPException
from starlette.requests import Request
from starlette.responses import Response

from custom_exceptions.custom_not_found import CustomNotFound
from dtos.auth import LoginReq, AuthDto
from services.auth_service import AuthService

router = APIRouter(tags=["auth"], prefix="/api/auth")


@router.get('/account')
async def get_account(service: AuthService, request: Request) -> AuthDto:
    try:
        use_header = False
        if request.cookies.get('access_token_cookie'):
            access_token = request.cookies.get('access_token_cookie')
        else:
            use_header = True
            access_token = request.headers.get('Authorization', None)

        account = service.get_account(access_token, use_header)
        return account
    except CustomNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post('/login')
async def login(request_data: LoginReq, service: AuthService, response: Response):
    try:
        token = service.login(request_data.username, request_data.password)
        response.set_cookie('access_token_cookie', token, httponly=True)
        return {'token': token}
    except CustomNotFound as e:
        raise HTTPException(status_code=404, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post('/register')
async def register(request_data: LoginReq, service: AuthService) -> AuthDto:
    user = service.register(request_data.username, request_data.password)

    return user
