import database.db_config as _config
import fastapi as _fastapi
from models.list import List

def task(tid: str):
    db = _config.SessionLocal()
    try:
        task = db.query(List).filter(List.TID == tid).first()
        if not task:
            raise _fastapi.HTTPException(status_code=404, detail="Not found task")

        db.delete(task)
        db.commit()

        return {"response": "success"}
    except Exception as e:
        db.rollback()
        return {"error": str(e)}
    finally:
        db.close()


if __name__ == "__main__":
    print(task("A9387A1124"))