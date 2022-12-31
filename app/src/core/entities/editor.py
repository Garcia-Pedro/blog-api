from src.core.usecases import register_account_editor

class EntityEditor:
    """_summary_
    """    
    def __init__(self) -> None:
        return None
    
    @classmethod
    def create_account_editor(self,data:dict,img):
       
        resp=register_account_editor(data,img)
        return resp