from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.exceptions import HTTPException

class MSResponse:
    """_summary_
    """    
    def __init__(self) -> None:
        return None

    @classmethod
    def msg_created_success(self,msg:str):
        return JSONResponse({"msg":msg},status_code=status.HTTP_201_CREATED,)
    
    @classmethod
    def msg_created_error(self,msg:str):
        return HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail=f"msg:{msg}")