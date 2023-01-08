import io
from app.src.infra.db import engine
from app.src.infra.models import Editor
from app.src.infra.feadback import MSResponse
from sqlmodel import Session, select
from sqlalchemy.orm import load_only


msresponses=MSResponse

def select_image_editor(id_editor: str):
    try:
        with Session(engine) as session:
            statement = select(Editor).options(
                load_only(
                    "img","img_type")
                    ).where(Editor.id_editor == "%s" % (id_editor))
            result = session.exec(statement).one()
            if result:
                img=io.BytesIO(result.img)
                return msresponses.return_file(img.read(),result.img_type)
            else:
                return msresponses.msg_request_not_found(msg="image not found")
    except Exception as exc:
        raise msresponses.msg_request_bad(f"error:{exc}")

