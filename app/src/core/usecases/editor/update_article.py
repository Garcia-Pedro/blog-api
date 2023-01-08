from app.src.infra.db import engine
from sqlmodel import Session, select
from app.src.infra.models import PostArticle
from app.src.infra.feadback import MSResponse


msresponse = MSResponse


def update_article_post(data, img, id_article, id_editor):
    try:
        with Session(engine) as session:
            statement = select(PostArticle).where(
                PostArticle.idArticle == "%s" % (id_article)).where(PostArticle.editor_id=="%s"%(id_editor))
            results = session.exec(statement)
            update_article = results.one()
            update_article.title = data['title']
            update_article.subtitle = data['subtitle']
            update_article.font = data['font']
            update_article.body = data['body']
            update_article.img = img["read"]
            update_article.img_name = img["img_filename"]
            update_article.img_type = img["img_type"]
            session.add(update_article)
            session.commit()
            session.refresh(update_article)
            return msresponse.msg_ok("article updated with success")

    except Exception as exc:
        raise msresponse.msg_created_error("error when updating article")
