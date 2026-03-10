# 1. Utiliser une image Python officielle (version légère)
FROM python:3.9-slim

# 2. Définir le répertoire de travail dans le conteneur
WORKDIR /app

# 3. Copier le fichier des dépendances dans le conteneur
COPY requirements.txt .

# 4. Installer les dépendances (la bibliothèque requests)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copier tout le code de ton dossier actuel (app.py) dans le conteneur
COPY . .

# 6. Indiquer la commande pour lancer ton script Python
CMD ["python", "app.py"]