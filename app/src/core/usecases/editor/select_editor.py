from app.src.infra.db import engine
from app.src.infra.models import Editor
from sqlmodel import Session, select
from sqlalchemy.orm import load_only
from app.src.infra.feadback import MSResponse

msresponse=MSResponse

def select_info_editor(id_editor):
    try:
        with Session(engine) as session:
            statement = select(Editor).where(Editor.id_editor == "%s" % (
                id_editor)).options(load_only("username", "email", "created_at"))
            result=session.exec(statement).one()
            return result
    except Exception as exc:
        raise msresponse.msg_request_bad(f"error:{exc}")

