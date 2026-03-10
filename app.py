import requests

def main():
    # URL de l'API suggérée dans l'exercice (Blagues aléatoires)
    url = "https://official-joke-api.appspot.com/random_joke"

    try:
        # Appel de l'API
        response = requests.get(url)

        # 1. Affiche le Status code (demandé dans le TP)
        print(f"Status code: {response.status_code}")

        # 2. Affiche le contenu de la réponse (demandé dans le TP)
        if response.status_code == 200:
            data = response.json()
            print("Response content (JSON):")
            print(data)
        else:
            print(f"Erreur lors de l'appel : {response.text}")

    except Exception as e:
        print(f"Une erreur est survenue : {e}")

if __name__ == "__main__":
    main()
