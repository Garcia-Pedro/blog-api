from typing import Optional
from fastapi import APIRouter
from app.src.interface import FastAPIAdapter


visitor_route=APIRouter(prefix="/global",tags=['visitor'])
adapter=FastAPIAdapter

@visitor_route.get("/view_article_all",tags=['visitor'])
async def view_articles():
    return adapter.view_articles()


@visitor_route.get("/view_article/{id_article}",tags=['visitor'])
async def view_article(id_article:str):
    return adapter.view_article(id_article)

@visitor_route.get("/view_article/image/{id_article}",tags=['visitor'])
async def view_image_article(id_article:str):
    return adapter.view_image_article(id_article)


@visitor_route.get("/search_article/query={search}",tags=['visitor'])
async def search_article(search:Optional[str]):
    return adapter.search_article(search)