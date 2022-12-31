from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.infra.requests.editor import editor_route


# API main
api = FastAPI(title="Blog API", description="API for the blog angola Comunica")

api.add_middleware(CORSMiddleware, 
                        allow_origins=["*"], 
                        allow_credentials=True, 
                        allow_methods=["*"], 
                        allow_headers=["*"])

api.include_router(editor_route,prefix="/blog",tags=['editor'])

