from sqlmodel import create_engine,Session
from src.infra.models import *
from urllib.parse import quote_plus
#database mysql
mysql_db_name="mysql+pymysql://root:%s@localhost/blogAPI"%(quote_plus('fredericodev@92424'))

#database sqlite
sqlite_file_name="blog_angocomunica.db"
sql_url=f"sqlite:///{sqlite_file_name}"
engine=create_engine(mysql_db_name,echo=True)
