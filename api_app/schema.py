from pydantic import BaseModel

# schema pour un identifiant
class User(BaseModel):
    username : str
    pwd : str

# schema pour le texte reçu dans la requête POST.
class TextInput (BaseModel):
    text : str
# pour la réponse JSON de notre API
class SentimentResponse (BaseModel):
    text : str
    sentiment : str
    score : float
    
    