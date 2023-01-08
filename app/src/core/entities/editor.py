from app.src.core.usecases import *

class EntityEditor:
    """_summary_
    """    
    def __init__(self) -> None:
        return None
    
    @classmethod
    def create_account_editor(self,data:dict,img):
       
        resp=register_account_editor(data,img)
        return resp
    
    @classmethod 
    def add_post_article(self,data:dict,img,id_editor):
        resp=register_article_post(data,img,id_editor)
        return resp

    @classmethod 
    def update_post_article(self,data:dict,img,id_article,id_editor):
        resp=update_article_post(data,img,id_article,id_editor)
        return resp
    
    @classmethod
    def delete_post_article(self,id_article:str,id_editor:str):
        resp=delete_article_post(id_article,id_editor)
        return resp

    @classmethod
    def view_info_editor(self,id_editor):
        resp=select_info_editor(id_editor)
        return resp
    
    @classmethod
    def view_image_editor(self,id_editor):
        resp= select_image_editor(id_editor)
        return resp
