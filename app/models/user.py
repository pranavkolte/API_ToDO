import sqlalchemy.ext.declarative as _declarative
import sqlalchemy as _sql
import datetime as _datetime

Base = _declarative.declarative_base()

class User(Base):
    __tablename__ = "user"
    id = _sql.Column(_sql.String, primary_key=True, index=True)
    name = _sql.Column(_sql.String, index=True)
    email = _sql.Column(_sql.String, unique=True, index=True)
    password = _sql.Column(_sql.String)
    time = _sql.Column(_sql.TIMESTAMP, default = _datetime.datetime.now())