from fastapi import FastAPI,HTTPException ,Depends,Header
from api_app.schema import SentimentResponse,   TextInput , User
import requests
import os
from dotenv import load_dotenv
from api_app.haggingface_client import analyse_sentiment

from jose import jwt,JWTError

load_dotenv()


HF_API_TOKEN = os.getenv('HUGGINGFACE_API_TOKEN')


# Configuration de JWT
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_user = {
    
        "username": "khadija",
        "password": "Elabbioui99"
    
}

app = FastAPI (title="Bienvenue à l'API d'analyse de sentiment",description="Une API simple pour analyser le sentiment de texte en utilisant Hugging Face Inference API.")

def get_star(label):
    for i in range(1,6):
        if f"{i} star" in label :
          
          return i 
        
def get_sentiment(label):
    
    rate = get_star(label)
    if rate in [1,2]:
        return "negatif"
    elif rate==3 :
         return "neutre"
    elif rate in [4,5]:
         return "positif"
    return "inconnu"
# def get_sentiment(label):
    # if '1 star' in label or '2 stars' in label:
    #     return "negatif"
    # if '3 stars' in label:
    #     return "neutre"
    # if '4 stars' in label or '5 stars' in label:
    #     return "positif"
    # return "indeterminé" 




# Endp

@app.post("/login") 
def verify_info_login(login : User) :
     if login.username == fake_user["username"] and login.pwd == fake_user["password"] :
         usrtoken = jwt.encode({},key=SECRET_KEY,algorithm=ALGORITHM)
         return usrtoken
     else :
         return { "message" : "Access Failed "}

    

@app.get('/verify') 
def verify_token(token : str = Header()):
  try:
      token_decode = jwt.decode(token=token,key=SECRET_KEY,algorithms=[ALGORITHM])
      return token_decode
  except JWTError:
      raise HTTPException(status_code=401,detail='Token lli 3titi invalide azin')


# # Endpoint Post /predict Protected with JWT
# @app.post("/predict_protected")
# async def predict_sentiment(request: TextInput, new_user : str = Depends(verify_token)):
#     text = request.text
#     if not text:
#         raise HTTPException(status_code=400, detail="Le champ 'text' ne peut pas être vide.")
    
#     response = analyse_sentiment(text)
#     if not isinstance(response, list):
#       return response        # renvoie l’erreur HF directement
   

#     top_prediction = response[0][0] 
    
#     # Extraire label et score
#     label = top_prediction.get("label")
   
#     score = get_star(label)
#     semntiment  = get_sentiment(label)
#     print(semntiment)
#     print(score)
#     return {"message": "Khadija, you’re a shining star"}


# endpoint Post /predict
@app.post("/predict",response_model=SentimentResponse)
async def predict_sentiment(request: TextInput):
    text = request.text
    if not text:
        raise HTTPException(status_code=400, detail="Le champ 'text' ne peut pas être vide.")
    
    response = analyse_sentiment(text)
    if not isinstance(response, list):
      return response        # renvoie l’erreur HF directement
   

    top_prediction = response[0][0] 
    
    # Extraire label et score
    label = top_prediction.get("label")
   
    score = get_star(label)
    semntiment  = get_sentiment(label)
    
    return  SentimentResponse (
            text=request.text,
            sentiment=semntiment,
            score=score
        )