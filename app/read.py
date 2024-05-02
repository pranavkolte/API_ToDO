import fastapi as _fastapi
import database.db_config as config
from models.user import User
from models.list import List
import sqlalchemy as _sql


def UID(email : str):
    try:

        db = config.SessionLocal()
        user = db.query(User).filter(User.email == email).first()
        if not user:
            raise _fastapi.HTTPException(status_code=404, detail="User not found")

        return {
            "UID": user.UID,
        }
    
    except Exception as error:
        return {"response" : f"{error}"}
    finally:
        db.close()

def alltask(UID : str):
    
    result = config.SessionLocal().query(List).filter(List.UID == UID).all()
    response = {}

    for idx, task in enumerate(result, start=1):
        response[idx] = {'TID': task.TID, 'name': task.name, 'description': task.description, 'Due': task.due}
    
    return response


if __name__ =='__main__':
    print(alltask("ed6ca046840450b021403a27bd8a334c3fa6c990"))