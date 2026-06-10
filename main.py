from fastapi import FastAPI
from routers.auth_routes import router as auth_router
from routers.notes import router as note_router
from routers.users import router as user_router
app = FastAPI()
app.include_router(auth_router)
app.include_router(note_router)
app.include_router(user_router)