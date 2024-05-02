import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative


class List(_declarative.declarative_base()):
    __tablename__ = "lists"
    TID = _sql.Column(_sql.String, primary_key=True, index=True)
    UID = _sql.Column(_sql.String, index=True)
    name = _sql.Column(_sql.String, index=True)
    description = _sql.Column(_sql.String , index=True)
    due = _sql.Column(_sql.DATETIME)