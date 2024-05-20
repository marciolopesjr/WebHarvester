import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_file(url, folder):
    local_filename = os.path.join(folder, url.split('/')[-1])
    # Faz o download do arquivo
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

def download_all_files_from_page(page_url, folder):
    # Faz a requisição HTTP para obter o conteúdo da página
    response = requests.get(page_url)
    response.raise_for_status()  # Verifica se houve algum erro na requisição

    # Analisa o conteúdo HTML da página
    soup = BeautifulSoup(response.content, 'html.parser')

    # Cria o diretório de destino, se não existir
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Encontra todos os links (tags <a>) na página
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            # Constrói a URL completa do arquivo
            file_url = urljoin(page_url, href)
            # Pode adicionar lógica para filtrar tipos de arquivos específicos, se necessário
            try:
                print(f'Baixando {file_url} ...')
                download_file(file_url, folder)
            except Exception as e:
                print(f'Erro ao baixar {file_url}: {e}')

# URL da página da qual deseja baixar os arquivos
page_url = 'https://exemplo.com/pagina-com-links'
# Diretório de destino para salvar os arquivos
download_folder = 'arquivos_baixados'

download_all_files_from_page(page_url, download_folder)
