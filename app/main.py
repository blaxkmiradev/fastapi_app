from fastapi import FastAPI
from app.routes import hello

app = FastAPI()

# Include router
app.include_router(hello.router)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}
