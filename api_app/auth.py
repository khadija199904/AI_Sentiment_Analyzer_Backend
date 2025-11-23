from fastapi import Header,HTTPException
from dotenv import load_dotenv
import os
from jose import jwt
from api_app.schema import User

load_dotenv()

# Configuration de JWT
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

fake_user = {
    
        "username": "khadija",
        "password": "Elabbioui99"
    
}

 
def create_token(login : User):
   if login.username == fake_user["username"] and login.password == fake_user["password"] :
         usrtoken = jwt.encode({},key=SECRET_KEY,algorithm=ALGORITHM)
         return usrtoken


def verify_token(token : str = Header()):
  try:
      token_decoded = jwt.decode(token=token,key=SECRET_KEY,algorithms=[ALGORITHM])
      return token_decoded
  except :
      raise HTTPException(status_code=401,detail='Token invalide azin')
  


