import sqlalchemy as _sql
import sqlalchemy.orm as _orm

HOST= "172.25.0.2" 
USER = "root"
PASS = "abcd"
DATABASE_NAME = "todoapi"



DATABASE_URL = f"mysql+mysqlconnector://{USER}:{PASS}@{HOST}/{DATABASE_NAME}"

engine = _sql.create_engine(DATABASE_URL)
SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
