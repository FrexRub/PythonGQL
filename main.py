from fastapi import FastAPI
from graphql_server import graphql_app
import uvicorn

app = FastAPI()
app.include_router(graphql_app, prefix='/graphql')


if __name__ == "__main__":
    uvicorn.run("main:app")