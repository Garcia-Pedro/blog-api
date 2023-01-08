from unittest import result
from src.infra.models import PostArticle
from src.infra.db import engine
from sqlmodel import Session, select
from sqlalchemy.orm import load_only
from src.infra.feadback import MSResponse


msresponses = MSResponse


def select_all_articles():
    try:
        with Session(engine) as session:
            statement = select(PostArticle).options(
                load_only("title", "subtitle", "body", "font", "create_at"))
            result = session.exec(statement).fetchall()
            if result:
                return result
            else:
                return msresponses.msg_request_not_found(msg="not found article")

    except Exception as exc:
        raise msresponses.msg_request_bad(f"error:{exc}")
