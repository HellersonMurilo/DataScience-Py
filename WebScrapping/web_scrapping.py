from bs4 import BeautifulSoup
import requests

# url para acesso
url = "https://g1.globo.com/"

# fazendo busca da requisicao HTTP
resposta = requests.get(url)

if resposta.status_code == 200:

    soup = BeautifulSoup(resposta.text, "html.parser")

    # encontrar todas as noticias
    noticias = soup.find_all("a", class_="feed-post-link")

    # print("Ultimas noticias do G1:")

    for index, noticia in enumerate(noticias):
        # escrevendo cada noticia
        print(f"{noticia.text}")
