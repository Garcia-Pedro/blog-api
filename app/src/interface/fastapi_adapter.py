from click import edit
from app.src.core.entities import EntityEditor
from app.src.core.entities import VisitorEntity

editor=EntityEditor()
visitor=VisitorEntity()

class FastAPIAdapter:
    """_summary_
    """    
    def __init__(self) -> None:
        return None

    #http://127.0.0.1:8000/blog/editor/create_account    
    @classmethod
    def create_account_editor(self,data:dict,img):
        return editor.create_account_editor(data,img)
    
    #http://127.0.0.1:8000/blog/editor/view_image/{id_editor}
    @classmethod
    def view_image_editor(self,id_editor):
        return editor.view_image_editor(id_editor)

    #http://127.0.0.1:8000/blog/editor/post/add
    @classmethod
    def add_post_article(self,data:dict,img,id_editor):
        return editor.add_post_article(data,img,id_editor)
    
    #http://127.0.0.1:8000/blog/editor/post/update-post/{id_post}
    @classmethod
    def update_post_article(self,data:dict,img,id_article,id_editor):
        return editor.update_post_article(data,img,id_article,id_editor)
    
    
    #http://127.0.0.1:8000/blog/editor/article/delete-post
    @classmethod
    def delete_post_article(self,id_article:str,id_editor:str):
        return editor.delete_post_article(id_article,id_editor)

    #http://127.0.0.1:8000/blog/editor/info
    @classmethod
    def view_info_editor(self,id_editor:str):
        return editor.view_info_editor(id_editor)

    #http://127.0.0.1:8000/blog/global/view_article_all
    @classmethod 
    def view_articles(self):
        return visitor.view_articles()
    
    #http://127.0.0.1:8000/blog/global/view_article/{id_article}
    @classmethod 
    def view_article(self,id_article):
        return visitor.view_article(id_article)
    

    #http://127.0.0.1:8000/blog/global/view_article/image/{id_article}
    @classmethod
    def view_image_article(self,id_article):
        return visitor.view_image_article(id_article)

    #http://127.0.0.1:8000/blog/editor/view_image/{id_editor}
    @classmethod
    def view_image_editor(self,id_editor):
        return editor.view_image_editor(id_editor)
    
    @classmethod
    def search_article(self,search):
        return visitor.search_article(search)