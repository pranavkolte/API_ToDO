
import read
import passlib.context as _passlib
import fastapi.security as _security
import jwt as _jwt
import datetime as _datetime
import hash

SECRET_KEY = "83daa0256a2289b0fb23693bf1f6034d44396675749244721a2b20e896e11662"
ALGORITHM = "HS256"


oauth2_scheme = _security.OAuth2PasswordBearer(tokenUrl="token")


def generate(data : dict, expires_delta : _datetime.timedelta = 15):
    to_encode = data.copy()
    expire = _datetime.datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_JWT = _jwt.encode(to_encode, SECRET_KEY , ALGORITHM)
    return encoded_JWT


def check_if_valid(token):
    try:
        payload = _jwt.decode(token, SECRET_KEY, ALGORITHM)
        expiration_time = _datetime.datetime.utcfromtimestamp(payload["exp"])
        if expiration_time > _datetime.datetime.utcnow() :
            return {'status' : 'authorised'}
    except _jwt.ExpiredSignatureError:
        return  {'status' : 'EXPIRED_TOKEN'}
    except _jwt.InvalidTokenError:
        return {'status' : 'INVALID_TOKEN'}


def user_auth(email: str, password : str): 
    user = read.user(email)
    if not user:
        return False
    
    if not hash.getSHA256(password) == user.password:
        return False
    return user

if __name__ == "__main__":
    print(user_auth("admin@gmail.com", "1234"))