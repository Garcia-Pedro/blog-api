from src.core.entities.editor import EntityEditor


editor=EntityEditor()

class FastAPIAdapter:
    """_summary_
    """    
    def __init__(self) -> None:
        return None

    #http://127.0.0.1:8000/blog/editor/create_account    
    @classmethod
    def create_account_editor(self,data:dict,img):
        return editor.create_account_editor(data,img)