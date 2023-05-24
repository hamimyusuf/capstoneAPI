from fastapi import FastAPI
from routes.register_route import router as RegisterRouter
from routes.login_route import router as LoginRouter
from routes.user_manage_route import router as UserManage
from routes.input_image_route import router as UploadImage
from routes.history_route import router as HistoryRouter
from routes.information_route import router as InformationRouter

app = FastAPI(
    title='Capstone'
)

app.include_router(RegisterRouter, tags=["Register New User"],prefix="/register")
app.include_router(LoginRouter, tags=["User Login"],prefix="/login")
app.include_router(UserManage, tags=["User Manage"],prefix="/manage")
app.include_router(UploadImage, tags=["Input Image"],prefix="/upload")
app.include_router(HistoryRouter, tags=["Data History"],prefix="/history")
app.include_router(InformationRouter, tags=["Data Information"],prefix="/information")

