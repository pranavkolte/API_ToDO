import fastapi as _fastapi
import fastapi as _fastapi
import hash as _hash
import datetime as _datetime

from models.user import User
from models.list import List
import database.db_config as _config

def user(name : str, email : str, password:str):
    db = _config.SessionLocal()
    try:
        user = db.query(User).filter(User.email == email).first()
        if user:
            raise _fastapi.HTTPException(status_code=422, detail="Email is already registered with us.")
        
        new_user = User(
            UID = _hash.getSHA1(f"{_datetime.datetime.now}{email}"),
            name = name,
            email = email,
            password = _hash.getSHA256(password),
        )

        db.add(new_user)
        db.commit()

        return {"response": "success"}
    except Exception as e:
        db.rollback()
        return {"error": str(e)}
    finally:
        db.close()
  
def task(UID, name, description, due):
    db = _config.SessionLocal()
    try:
        task_id =  _hash.get_SHA1_limit(f"{name}{UID}")
        list = db.query(List).filter(List.TID == task_id).first()
        if list:
            raise _fastapi.HTTPException(status_code=422, detail="Task is already exist")
        
        new_task = List(
            TID =task_id,
            UID = UID,
            name = name,
            description = description,
            due = due,
        )

        db.add(new_task)
        db.commit()

        return {"response": "success"}
    except Exception as e:
        db.rollback()
        return {"error": str(e)}
    finally:
        db.close()
