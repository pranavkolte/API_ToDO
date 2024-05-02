import sqlalchemy.ext.declarative as _declarative
import sqlalchemy as _sql

class User(_declarative.declarative_base()):
    __tablename__ = "users"
    UID = _sql.Column(_sql.String, primary_key=True, index=True)
    name = _sql.Column(_sql.String, index=True)
    email = _sql.Column(_sql.String, unique=True, index=True)
    password = _sql.Column(_sql.String)