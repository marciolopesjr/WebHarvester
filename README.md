### WebHarvester - Colha Arquivos da Web com Facilidade

### Descrição

WebHarvester é um script Python que facilita a coleta de arquivos de páginas da web. Com ele, você pode baixar todos os arquivos vinculados em uma página da web com apenas alguns comandos.

## Funcionalidades

- Faz a requisição HTTP para obter o conteúdo da página web.
- Analisa o HTML da página para encontrar todos os links.
- Baixa os arquivos linkados e os salva em um diretório especificado.

## Requisitos

- Python 3.x
- Bibliotecas Python: `requests`, `beautifulsoup4`

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/marciolopesjr/WebHarvester.git
   cd WebHarvester.git
2. Instale as dependências:
   ```bash
   pip install requests beautifulsoup4
3. Edite o script web_harvester.py para especificar a URL da página da qual deseja baixar os arquivos e o diretório de destino:
   ```bash
      # URL da página da qual deseja baixar os arquivos
     page_url = 'https://exemplo.com/pagina-com-links'
     # Diretório de destino para salvar os arquivos
     download_folder = 'arquivos_baixados'
4. Execute o script:
   ```bash
   python web_harvester.py

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Feito com ♥ e Python por Márcio Lopes.
