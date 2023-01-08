from fastapi.responses import JSONResponse,Response
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
    def msg_request_not_found(self,msg:str):
        return JSONResponse({"msg":msg},status_code=status.HTTP_404_NOT_FOUND,)


    @classmethod
    def msg_created_error(self,msg:str):
        return HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail=f"msg:{msg}")
    
    @classmethod
    def msg_request_bad(self,msg:str):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"msg:{msg}")

    @classmethod
    def msg_ok(self,msg:str):
        return JSONResponse({"msg":msg},status_code=status.HTTP_200_OK)
    
    @classmethod
    def return_file(self,file,file_type:str):
        return Response(file,status_code=status.HTTP_200_OK,media_type=file_type)