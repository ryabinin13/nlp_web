from app import app
from app.routers.users import user_router
from app.routers.home import home_router

app.include_router(user_router)
app.include_router(home_router)

