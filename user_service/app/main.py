from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.models.database import get_db
from app.routes import user_routes

app = FastAPI()

@app.on_event("startup")
def on_startup():
    get_db()

# Handler global para 422
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={
            "message": "Error en la validación de datos",
            "errors": exc.errors()
        },
    )

app.include_router(user_routes.router)

@app.get("/")
def read_root():
    return {"Hello": "User Service"}
