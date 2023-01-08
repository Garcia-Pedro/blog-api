from src.infra.db import engine
from sqlmodel import Session, select
from src.infra.models import PostArticle
from src.infra.feadback import MSResponse


msresponse=MSResponse

def delete_article_post(id_article: str, id_editor: str):
    try:
        with Session(engine) as session:
            statement = select(PostArticle).where(PostArticle.idArticle == f"{id_article}").where(
                PostArticle.editor_id == f"{id_editor}")
            results=session.exec(statement)
            delete_article=results.one()

            session.delete(delete_article)
            session.commit()
            return msresponse.msg_ok("article delete with success")
    except Exception as exc:
        raise msresponse.msg_request_bad(f"{exc}")

