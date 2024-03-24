import requests
from bs4 import BeautifulSoup

# URL de la page à scraper
url = "https://example.com"

# Faire la requête GET
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Analyser le contenu HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extraire les liens
    links = soup.find_all('a')
    
    # Afficher les liens
    for link in links:
        print(link.get('href'))
else:
    print("La requête a échoué.")
