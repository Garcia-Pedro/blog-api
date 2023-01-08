from sqlalchemy import Text
from sqlmodel import SQLModel, Field
import sqlalchemy as sa
from sqlalchemy import Column, String, ForeignKey
import typing as typer
import datetime as date
from typing import Optional

# table post article
class PostArticle(SQLModel, table=True):
    __tablename__ = "PostArticle"

    idArticle: str = Field(default=None, primary_key=True,
                           nullable=False, unique=True)
    title: str = Field(default=None, nullable=False)
    subtitle: str = Field(default=None, nullable=False)
    body: str = Field(default=None, nullable=False)
    font: str = Field(default=None, nullable=False)
    create_at: date.datetime = Field(
        default_factory=date.datetime.utcnow, nullable=False)
    img: Optional[bytes] = Field(
        default=None, sa_column=sa.Column(sa.LargeBinary))
    img_name: Optional[str] = Field(default=None, nullable=False)
    img_type: str = Field(default=None, nullable=False)
    editor_id: str = Field(default=None, sa_column=Column(String(150), ForeignKey(
        "Editor.id_editor", ondelete="CASCADE", onupdate="CASCADE")))
