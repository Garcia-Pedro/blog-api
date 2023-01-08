from fastapi import APIRouter,UploadFile,File
from starlette.requests import Request
from src.interface import FastAPIAdapter
from fastapi.exceptions import HTTPException
from fastapi.security.oauth2 import OAuth2PasswordBearer
from src.infra.requests.depends import EditorToken
from fastapi import Depends

#api route editor
editor_route=APIRouter(prefix="/editor",tags=["editor"])
adapter=FastAPIAdapter()
editor_token=EditorToken
oauth2_token=OAuth2PasswordBearer(tokenUrl="login")

#add editor
#http://127.0.0.1:8000/blog/editor/create_account
@editor_route.post("/create_account",tags=['editor'])
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

#login editor
#http://127.0.0.1:8000/blog/editor/login
@editor_route.post("/login",tags=['editor'])
async def login_editor(form_data:Request):
    data=await form_data.form()
    return editor_token.create_access_token(data)


#add post in blog
#http://127.0.0.1:8000/blog/editor/article/add-post
@editor_route.post("/article/add-post",tags=['editor'])
async def add_post_article(form_data:Request,image:UploadFile=File(...),
                                token:str=Depends(oauth2_token)):

    data=await form_data.form()
    id_editor=editor_token.get_current_user(token)
    img_article={
        "read":await image.read(),
        "img_type":image.content_type,
        "img_filename":image.filename

    }
    return adapter.add_post_article(data,img_article,id_editor)


#update post in blog
#http://127.0.0.1:8000/blog/editor/article/update-post
@editor_route.put("/article/update-post/{id_article}",tags=['editor'])
async def update_post_article(id_article:str,form_data:Request,image:UploadFile=File(...),
                                token:str=Depends(oauth2_token)):

    data=await form_data.form()
    id_editor=editor_token.get_current_user(token)
    img_article={
        "read":await image.read(),
        "img_type":image.content_type,
        "img_filename":image.filename

    }
    return adapter.update_post_article(data,img_article,id_article,id_editor)


#delete post in blog
#http://127.0.0.1:8000/blog/editor/article/delete-post
@editor_route.delete("/article/delete-post/{id_article}",tags=['editor'])
async def delete_post_article(id_article:str,token:str=Depends(oauth2_token)):
    id_editor=editor_token.get_current_user(token)
    return adapter.delete_post_article(id_article,id_editor)


#http://127.0.0.1:8000/blog/editor/info
@editor_route.get("/view_info_editor",tags=['editor'])
async def view_info_editor(token:str=Depends(oauth2_token)):
    id_editor=editor_token.get_current_user(token)
    return adapter.view_info_editor(id_editor)


#http://127.0.0.1:8000/blog/editor/view_image/{id_editor}
@editor_route.get("/view_image/{id_editor}",tags=['editor'])
async def view_image_editor(id_editor:str):
    return adapter.view_image_editor(id_editor)


