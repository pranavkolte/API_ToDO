import sqlalchemy as _sql
import sqlalchemy.orm as _orm

HOST= "127.0.0.1" 
USER = "root"
PASS = ""
DATABASE_NAME = "todoapi"

DATABASE_URL = f"mysql+mysqlconnector://{USER}@{HOST}/{DATABASE_NAME}"

engine = _sql.create_engine(DATABASE_URL)
SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
