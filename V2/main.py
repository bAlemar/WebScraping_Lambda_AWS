from selenium import webdriver
from tempfile import mkdtemp
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

import json
import boto3


def upload_s3(dict_resultado):
    s3 = boto3.client('s3')
    bucket = 'webscraping-zap'

    fileName = 'Resultados' + '.json'     
    
    uploadByteStream = bytes(json.dumps(dict_resultado).encode('UTF-8'))

    s3.put_object(Bucket=bucket,
                  Key = fileName,
                  Body = uploadByteStream)
    print('Put Complete')

def extract_soup(soup):
    """
    Essa função extrai a informações do site por meio da SOPA
    Vale destacar que podemos retirar + informações basta acrescentar sua localização

    Argumentos:
    - soup: Sopa com conteúdo do site(html.parser)
    """

    dict_resultado = {'preco_imovel':[],
                    'metro_quadrado':[],
                    'localizacao_rua':[]}
    lista_anuncios = soup.find_all('div',class_='listing-wrapper__content')
    print(lista_anuncios)
    #Tentando percorrer os anuncios:
    card_content = lista_anuncios[0].find_all('div',class_='l-card__content')

    for i in card_content:
        preco_imovel = i.find_all('p',class_="l-text l-u-color-neutral-28 l-text--variant-heading-small l-text--weight-bold undefined")[0].text
        metro_quadrado = i.find_all('p',class_='l-text l-u-color-neutral-28 l-text--variant-body-small l-text--weight-regular card__amenity')[0].text
        localizacao_rua = i.find_all('p',class_='l-text l-u-color-neutral-28 l-text--variant-body-small l-text--weight-regular card__street')[0].text
        dict_resultado['preco_imovel'].append(preco_imovel)
        dict_resultado['metro_quadrado'].append(metro_quadrado)
        dict_resultado['localizacao_rua'].append(localizacao_rua)
    return dict_resultado

def handler(event=None, context=None):
    options = webdriver.ChromeOptions()
    service = webdriver.ChromeService("/opt/chromedriver")

    options.binary_location = '/opt/chrome/chrome'
    options.add_argument("--headless=new")
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--no-zygote")
    options.add_argument(f"--user-data-dir={mkdtemp()}")
    options.add_argument(f"--data-path={mkdtemp()}")
    options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
    options.add_argument("window-size=1920,1080")
    chrome = webdriver.Chrome(options=options, service=service)
    url='https://www.zapimoveis.com.br/venda/galpao-deposito-armazem/rj+rio-de-janeiro+zona-norte+s-cristovao/?__ab=seo-texts:control,exp-aa-test:control,deduplication:select,new-area-logada:variant,preco-metro-quadrado:deslog&transacao=venda&onde=,Rio%20de%20Janeiro,Rio%20de%20Janeiro,Zona%20Norte,S%C3%A3o%20Crist%C3%B3v%C3%A3o,,,neighborhood,BR%3ERio%20de%20Janeiro%3ENULL%3ERio%20de%20Janeiro%3EZona%20Norte%3ESao%20Cristovao,-22.899642,-43.222749,&tipos=galpao_comercial&pagina=1'
    chrome.get(url)
    #Time para não dar erro
    time.sleep(5)
    
    # Define a porcentagem desejada (70% neste caso)
    scroll_percentage = 20
    
    # Simulação do Scroll
    for i in range(18):
        # Calcula a altura total da página
        total_height = chrome.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")
        # Calcula a posição em pixels para rolar até a porcentagem desejada
        scroll_position = int((scroll_percentage / 100) * total_height)
        # Rola até o final da página
        chrome.execute_script(f"window.scrollTo(0, {scroll_position});")
        
        #Time Sleep Necessário se não vai direto
        time.sleep(1)
        
        if scroll_percentage > 50:
            scroll_percentage +=3
        else:
            scroll_percentage += 5


    time.sleep(3)

    # Obtém o HTML após o scroll
    html = chrome.page_source

    # Criando um objeto BeautifulSoup para analisar o HTML
    soup = BeautifulSoup(html, 'html.parser')
    resultado = extract_soup(soup)
    upload_s3(resultado)
    
    #Fechando Chrome
    chrome.close()
    chrome.quit()




    return {
            'statusCode': 200,
            'body': 'Completo'
            }