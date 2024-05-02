import fastapi as _fastapi
import database.db_config as _config

import hash as _hash
from models.list import List

def task(UID, name, description, due):
    db = _config.SessionLocal()
    try:
        # TODO elimnate duplication
        task_id =  _hash.get_SHA1_limit(f"{name}{UID}")
        list = db.query(List).filter(List.TID == task_id).first()
        if  list:
            list.TID = task_id
            list.UID = UID
            list.description = description
            list.due = due
        else:
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


if __name__ == "__main__":
    print(task("7c40eb71b34356ba0de8112cb68ad196fdef1f23", "FOFO", "make candles", "12/06/2024"))