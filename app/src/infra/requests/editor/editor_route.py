from fastapi import APIRouter,UploadFile,File
from starlette.requests import Request
from src.interface import FastAPIAdapter
from fastapi.exceptions import HTTPException

#api route editor
editor_route=APIRouter(prefix="/editor",tags=["editor"])
adapter=FastAPIAdapter()

#add editor
#http://127.0.0.1:8000/blog/editor/create_account
@editor_route.post("/create_account")
async def create_account_editor(form_data:Request,image:UploadFile=File(...)):
    data=await form_data.form()
    img_editor={
        "read":await image.read(),
        "img_type":image.content_type,
        "img_filename":image.filename

    }
    if data["password"]==data["confirm_password"]:
        return adapter.create_account_editor(data,img_editor)
    else:
        raise HTTPException(406,
                {"msg":"password and confirm_password is not equal"})
