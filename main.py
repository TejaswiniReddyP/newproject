from fastapi import FastAPI
from database import engine, Base
from routes import router


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(router, prefix="/api")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.2', port=8000)