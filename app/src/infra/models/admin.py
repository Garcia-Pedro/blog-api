from sqlmodel import Field, SQLModel
import sqlalchemy as sa
from typing import Optional
import datetime as date

# table editor


class Admin(SQLModel, table=True):
    __tablename__ = "Admin"

    id_admin: str = Field(default=None, primary_key=True,
                           nullable=False, unique=True)
    username: str = Field(default=None, nullable=False,
                          unique=True, min_length=4)
    email: str = Field(default=None, nullable=False,
                       unique=True, max_length=100)
    password: str = Field(default=None, nullable=False)
    img: Optional[bytes] = Field(
        default=None, sa_column=sa.Column(sa.LargeBinary))
    img_name: Optional[str] = Field(default=None, nullable=False)
    img_type: str = Field(default=None, nullable=False)
    created_at: date.datetime = Field(
        default_factory=date.datetime.utcnow, nullable=False)
