# Projet d'Analyse de Sentiments - Partie Backend (API FastAPI)

Ce répertoire contient le code source de l'API backend. Il s'agit d'une micro-API construite avec **FastAPI** qui fournit un service d'analyse de sentiments sécurisé par authentification JWT et connecté à l'API d'inférence de Hugging Face.

## Structure de Backend
```bash
AI_Sentimant_Analyzer/
│
├── api_app/                  # Code principal de l'API
│   ├── __init__.py
│   ├── auth.py               # Gestion JWT / authentification
│   ├── huggingFace_client.py # Intégration Hugging Face Inference API
│   ├── main.py               # Application FastAPI et endpoints
│   ├── schema.py             # Schémas Pydantic (User, etc.)
│   └── Dockerfile            # Dockerfile pour le backend
│
├── tests/                    
│   ├── test_api.py           # Tests endpoints FastAPI
│   └── test_unit.py          # Tests unitaires 
│
├── .gitignore                
├── requirements.txt          
└── README.md                 
```
## Fonctionnalités 
-   **Classification de Sentiment** : Le score retourné par Hugging Face est simplifié en trois catégories :
    -   `negatif` (pour les scores 1 ou 2)
    -   `neutre` (pour le score 3)
    -   `positif` (pour les scores 4 ou 5)
-   **Authentification JWT** : Un endpoint `POST /login` pour générer un jeton d'accès sécurisé.
-   **Endpoint Protégé** : Un endpoint `POST /predict` qui nécessite un jeton JWT valide pour être utilisé.
-   **Intégration d'IA Externe** : Communication avec l'API de **Hugging Face** pour analyser le sentiment d'un texte.
-   **Gestion des Erreurs** : Gestion robuste des erreurs potentielles lors de l'appel au service externe.
-   **Support Docker** : Fichier `Dockerfile` pour une conteneurisation facile.
-   **Tests Unitaires** : Tests intégrés avec `Pytest`.

### Bien sûr ! Voici la version formatée en Markdown. Vous pouvez la copier-coller directement.

code
Markdown
download
content_copy
expand_less
### Workflow d'Authentification JWT 

1.  **Connexion** : L'utilisateur envoie son email et son mot de passe au serveur. Si les informations sont correctes, le serveur lui renvoie un **jeton (JWT)** unique et sécurisé. Le navigateur le sauvegarde.

2.  **Requête Protégée** : Pour accéder à une page protégée, le navigateur envoie la requête en joignant automatiquement le **jeton JWT** (comme un badge d'accès).

3.  **Vérification** : Le serveur reçoit la requête, vérifie que le jeton est valide (ni faux, ni expiré). Si c'est bon, il donne l'accès à la page. Sinon, il le refuse.

## 1. Guide d'Installation

### Prérequis

-   Docker (pour l'approche par conteneurisation)
-   Un compte [Hugging Face](https://huggingface.co/) avec une clé d'API.

### Installation Locale

1.  **Clonez le dépôt** (si ce n'est pas déjà fait) 
    ```bash
    git clone <URL_DU_PROJET>
    ```

2.  **Créez un environnement virtuel et activez-le**
    ```bash
    # Pour macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # Pour Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Installez les dépendances Python**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurez vos variables d'environnement**
    Créez un fichier nommé `.env` à la racine du dossier `backend/` et remplissez-le avec vos informations :
    ```env
    # Clé secrète pour l'encodage JWT (générez une chaîne de caractères aléatoire et sécurisée)
    SECRET_KEY="votre_super_cle_secrete"

    # Votre clé d'API Hugging Face
    HUGGING_FACE_API_KEY="hf_xxxxxxxxxxxxxxxxxxxxxxxx"
    ```

## Lancement du Serveur

Une fois l'installation et la configuration terminées, vous pouvez lancer le serveur de développement avec Uvicorn.

```bash
uvicorn api_app.main:app --reload
```

## Tester les Endpoints avec Postman

Pour vérifier que l'API fonctionne correctement, vous pouvez utiliser [Postman](https://www.postman.com/downloads/). Voici comment tester les deux endpoints principaux : `POST /login` et `POST /predict`.

### Prérequis
-   Avoir Postman installé.
-   S'assurer que le serveur backend est en cours d'exécution (par exemple, sur `http://localhost:5000`).

---

### 1. Tester l'Endpoint de Connexion (`/login`)

Cet endpoint permet à un utilisateur de s'authentifier et de recevoir un jeton JWT en retour.

   **Réponse réussie :**
![Réponse réussie de /login avec un token JWT](/images/Postman_test_login.png)

 **Important : Copiez la valeur du `token` reçu.**

---

### 2. Tester l'Endpoint (`/predict`)

**Réponse réussie de l'endpoint :**
![Réponse réussie de /predict avec le sentiment et le score](/images/Postman_test_predict.png)

---

## Tests Backend

Pour lancer **tous les tests** (unitaires et API) :

```bash
python -m pytest -v
```
## Docker Backend
Pour créer et lancer le container Docker du backend :
# Depuis le dossier api_app
```bash
docker build -t sentiment-backend .
docker run -p 8000:8000 sentiment-backend
```
---

## Frontend

L'application **AI Sentiment Analyzer** dispose d'un **frontend séparé** développé en **React.js**.  
Pour utiliser l'application complète, vous pouvez consulter le **repo frontend** ici :  
[Frontend Repository](https://github.com/khadija199904/AI_Sentiment_Analyzer_frontend)

> Le frontend interagit avec ce backend pour afficher les résultats d'analyse de sentiment en temps réel.

---


## Auteur

**Nom :** KHADIJA ELABBIOUI  
**Email :** khadija.elabbioui1999@gmail.com  
**LinkedIn :** [linkedin.com/in/khadija-elabbioui](https://www.linkedin.com/in/khadija-elabbioui-308499216/)  
**GitHub :** [github.com/ton-github](https://github.com/khadija199904)

> N'hésitez pas à me contacter pour toute question ou suggestion concernant ce projet.