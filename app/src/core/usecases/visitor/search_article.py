from unittest import result
from app.src.infra.db import engine
from app.src.infra.models import PostArticle
from app.src.infra.feadback import MSResponse
from sqlmodel import Session, select,col
from sqlalchemy.orm import load_only


msresponses=MSResponse

def search_article_query(search: str):
    try:
        with Session(engine) as session:
            statement = select(PostArticle).options(
                load_only(
                    "title", "subtitle", "body", "font", "create_at")
                    ).where(
                        PostArticle.title.like("%{}%".format(search))).limit(
                            5).order_by(PostArticle.title)
            result = session.exec(statement).all()
            if result:
                return result
            else:
                return msresponses.msg_request_not_found(msg="not found article")
    except Exception as exc:
        raise msresponses.msg_request_bad(f"error:{exc}")

