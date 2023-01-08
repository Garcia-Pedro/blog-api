from src.core.usecases import *


class VisitorEntity:
    """_summary_
    """    
    def __init__(self) -> None:
        return None
    

    @classmethod 
    def view_articles(self):
        resp= select_all_articles()
        return resp
    
    @classmethod 
    def view_article(self,id_article):
        resp= select_one_article(id_article)
        return resp
    
    @classmethod 
    def view_image_article(self,id_article):
        resp= select_image_article(id_article)
        return resp

    @classmethod
    def search_article(self,search):
        resp=search_article_query(search)
        return resp