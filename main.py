from typing import Union
from fastapi import FastAPI
from users.routes import user_router

app = FastAPI()
app.title = "Investsphere API"

app.include_router(user_router)
