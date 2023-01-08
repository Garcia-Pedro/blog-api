from unittest import result
from app.src.infra.db import engine
from app.src.infra.models import PostArticle
from app.src.infra.feadback import MSResponse
from sqlmodel import Session, select
from sqlalchemy.orm import load_only


msresponses=MSResponse

def select_one_article(id_article: str):
    try:
        with Session(engine) as session:
            statement = select(PostArticle).options(
                load_only(
                    "title", "subtitle", "body", "font", "create_at")
                    ).where(PostArticle.idArticle == "%s" % (id_article))
            result = session.exec(statement).one()
            if result:
                return result
            else:
                return msresponses.msg_request_not_found(msg="not found article")
    except Exception as exc:
        raise msresponses.msg_request_bad(f"error:{exc}")

