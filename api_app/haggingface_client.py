import os 
import requests
from dotenv import load_dotenv
import time

# chargement des variables de .env
load_dotenv()

# URL du model geted with inference api in hugging face
API_URL = "https://router.huggingface.co/hf-inference/models/nlptown/bert-base-multilingual-uncased-sentiment"

# Récupérer la TOKEN d'API
HF_API_TOKEN = os.getenv('HUGGINGFACE_API_TOKEN')

if not HF_API_TOKEN:
    raise ValueError("La clé d'API Hugging Face n'est pas définie. Veuillez la mettre dans le fichier .env")


# praparer les en-têtes pour l'authentification
headers = {"Authorization": f"Bearer {HF_API_TOKEN}",}

def analyse_sentiment(text):
    if not text :
        return None
    payload = {"inputs": text}
    
    try:
        hf_response = requests.post(API_URL , headers=headers,json=payload,timeout=30)
       
    except requests.exceptions.RequestException as err:
        return {"error": f"Erreur réseau ou serveur indisponible: {err}"}
    
    # handle status codes
    if hf_response.status_code == 401:
        return {"error": "Clé API incorrecte (401)"}

    if hf_response.status_code == 404:
        return {"error": "Modèle introuvable (404)"}

    if hf_response.status_code == 503:
            time.sleep(30)
            return {"error": "Modèle en cours de chargement, nouvelle tentative dans 30 secondes (503)"}
    if hf_response.status_code != 200:
        return {"error": f"Erreur inconnue {hf_response.status_code}"}
    
    return hf_response.json()

    

