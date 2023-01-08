from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.src.infra.requests.editor import editor_route
from app.src.infra.requests.visitor import visitor_route

# API main
api = FastAPI(title="Blog API", description="API for the blog angola Comunica")

@api.get("/")
def index():
    return {
        "created_by":"Frederico Macau",
        "created_at":"07/01/2023",
        "name":"blog api"
    }

api.add_middleware(CORSMiddleware, 
                        allow_origins=["*"], 
                        allow_credentials=True, 
                        allow_methods=["*"], 
                        allow_headers=["*"])

api.include_router(editor_route,prefix="/blog",tags=['editor'])
api.include_router(visitor_route,prefix="/blog",tags=['visitor'])
