from app.src.infra.db import engine
from app.src.infra.models import PostArticle
from sqlmodel import Session
import uuid
from app.src.infra.feadback import MSResponse


#responses
msresponse=MSResponse

#register_article_post
def register_article_post(data,img,id_editor):
    try:
        with Session(engine) as conn:
            values=PostArticle(
                idArticle=uuid.uuid4().hex,
                title=data['title'],
                subtitle=data['subtitle'],
                font=data['font'],
                body=data['body'],
                img=img["read"],
                img_name=img["img_filename"],
                img_type=img["img_type"],
                
                editor_id=id_editor

            )
            conn.add(values)
            conn.commit()
            return msresponse.msg_created_success("create article with success")
        
    except Exception as exc:
        raise msresponse.msg_created_error(msg=f"{exc}")

