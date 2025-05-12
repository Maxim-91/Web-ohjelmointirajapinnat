from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import controllers.restaurant_ratings
from controllers import auth_controller

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'],
                   allow_headers=['*'])

app.include_router(controllers.restaurant_ratings.router)
app.include_router(controllers.auth_controller.router)
