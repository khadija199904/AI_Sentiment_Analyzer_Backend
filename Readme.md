# Projet d'Analyse de Sentiments - Partie Backend (API FastAPI)

Ce répertoire contient le code source de l'API backend. Il s'agit d'une micro-API construite avec **FastAPI** qui fournit un service d'analyse de sentiments sécurisé par authentification JWT et connecté à l'API d'inférence de Hugging Face.

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

Une fois l'installation et la configuration terminées, vous pouvez lancer le serveur de développement avec uvicorn.

```bash
uvicorn api_app.main:app --reload
```