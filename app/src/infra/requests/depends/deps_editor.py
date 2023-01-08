from bcrypt import checkpw
import jwt

from app.src.infra.db import engine
from sqlmodel import Session, select
from app.src.infra.models import Editor
from app.src.infra.feadback import MSResponse

#constants
SECRET="9c1f5e6705012fdc76df5717dfb979a23d7b66f48ee24662f8e4f710730fd6f1"
ALGORITHM="HS256"
response=MSResponse


#class to handle dependencies and author token "editor"

class EditorToken:
    """_summary_
    """    
    @classmethod
    def __verify_password(cls,password:str,password_hash:str):
        result=checkpw(password.encode("utf-8"),password_hash.encode("utf-8"))
        return  True if result else False

    #check the user in the database
    @classmethod 
    def __verify_user(cls, username):
        
        #created session with db
        with Session(engine) as session:
            statement=select(Editor.id_editor,Editor.username,Editor.password)
            return session.exec(statement.where(Editor.username==f"{username}")).fetchone()
    

    @classmethod
    def __authenticate_user(cls,data):
        user=cls.__verify_user(data['username'])
        if user:
            if cls.__verify_password(data['password'],user['password']):
                return user
            else:
                return False
        else:
            return False
        

    #create publisher access token
    @classmethod
    def create_access_token(cls,data):
        user_auth=cls.__authenticate_user(data)
        if user_auth:
            try:
                values={"id_editor":user_auth['id_editor']}
                token=jwt.encode(values,SECRET,ALGORITHM)
                return response.msg_ok(msg={"access_token":token,"token_type":"Bearer"})
            except (Exception) as exc:
                raise response.msg_created_error({"error":f"{exc}"})
        else:
            raise response.msg_request_bad(msg="username or password is invalid!!")


    
    @classmethod
    def get_current_user(cls,token):
        try:
            payload=jwt.decode(token,SECRET,ALGORITHM)
            return payload.get('id_editor')
        except (Exception) as exc:
            raise response.msg_request_bad(msg=f"{exc}")