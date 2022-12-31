from src.infra.db import engine
from src.infra.models import Editor
import uuid
from src.infra.feadback import MSResponse
from sqlmodel import Session
import bcrypt

#responses
msresponse=MSResponse

def encode_password(password:str):
    return bcrypt.hashpw(password.encode(),bcrypt.gensalt())

def register_account_editor(data:dict,img:dict):

    try:
        with Session(engine) as conn:
            add_editor=Editor(
                id_editor=uuid.uuid4().hex,
                username=data['username'],
                email=data['email'],
                password=encode_password(data["password"]),
                img=img["read"],
                img_name=img["img_filename"],
                img_type=img["img_type"]
            )
            conn.add(add_editor)
            conn.commit()
            return msresponse.msg_created_success("created with success")


    except Exception as exc:
        raise msresponse.msg_created_error(exc)

