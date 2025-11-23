from fastapi import FastAPI,HTTPException ,Depends,Header,Form
from api_app.schema import SentimentResponse,   TextInput , User
import requests
import os
from dotenv import load_dotenv
from api_app.haggingface_client import analyse_sentiment
from jose import jwt
from api_app.auth import create_token,verify_token
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI (title="Bienvenue à l'API d'analyse de sentiment",description="Une API simple pour analyser le sentiment de texte en utilisant Hugging Face Inference API.")


# --- Configuration CORS pour autoriser le frontend ---
origins = [
    "http://localhost:3000",  
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Autorise toutes les méthodes (GET, POST, etc.)
    allow_headers=["*"],  # Autorise tous les en-têtes
)



# Fonction pour extraire le nombre d'étoiles
def get_star(label):
    for i in range(1,6):
        if f"{i} star" in label :
          
          return i 
# Fonction pour extraire le sentiment 
def get_sentiment(label):
    
    rate = get_star(label)
    if rate in [1,2]:
        return "negatif"
    elif rate==3 :
         return "neutre"
    elif rate in [4,5]:
         return "positif"
    return "inconnu"



# Endpoint login

@app.post("/login") 
async def login(user_login : User):
    
     usertoken = create_token(user_login) 
     if usertoken is not None :
         return {"access_token" :usertoken}
     else :
         return { "message" : "Access Failed "}


# Endpoint Post /predict Protected with JWT
@app.post("/predict_protected",response_model=SentimentResponse)
async def predict_sentiment(request: TextInput, new_user : str = Depends(verify_token)):
    text = request.text
    if not text:
        raise HTTPException(status_code=400, detail="Le champ 'text' ne peut pas être vide.")
    
    response = analyse_sentiment(text)
    if not isinstance(response, list):
      return response       
   

    top_prediction = response[0][0] 
    
    # Extraire label et score
    label = top_prediction.get("label")
   
    score = get_star(label)
    semntiment  = get_sentiment(label)
    
    return SentimentResponse (
            sentiment=semntiment,
            score=score
        )


# endpoint Post /predict
@app.post("/predict",response_model=SentimentResponse)
async def predict_sentiment(request: TextInput):
    text = request.text
    if not text:
        raise HTTPException(status_code=400, detail="Le champ 'text' ne peut pas être vide.")
    
    response = analyse_sentiment(text)
    if not isinstance(response, list):
      return response        
   

    top_prediction = response[0][0] 
    
    # Extraire label et score
    label = top_prediction.get("label")
   
    score = get_star(label)
    semntiment  = get_sentiment(label)
    
    return  SentimentResponse (
            sentiment=semntiment,
            score=score
        )