import requests
from bs4 import BeautifulSoup


def handler(event=None, context=None):

    url = "https://example.com/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text,'html.parser')

    titulo = soup.find('title').text
    
    print(titulo)
    return {
        'statusCode':200,
        'body': titulo
    }