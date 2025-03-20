# Download YouTube Video API

Esta é uma API construída com FastAPI para baixar vídeos do YouTube usando `pytubefix`.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- Python 3.8 ou superior
- `pip` (gerenciador de pacotes do Python)
- `virtualenv` (recomendado para criar um ambiente isolado)

## Instalação

### 1 Clone o repositório:

```bash
git clone https://github.com/gabriel-engelles/download-yt-video.git
cd download-yt-video
```

### 2 Crie e ative um ambiente virtual:

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 3 Instale as dependências:

```bash
pip install -r requirements.txt
```

## Como usar

### 1 Inicie a api:

```bash
uvicorn app.main:app --reload --port 8001
```

### 2 Baixar um vídeo do YouTube:

***diretamente atráves da url***

```bash
http://127.0.0.1:8001/baixar_video/?url=<URL_DO_VIDEO>
```

***ou atráves do swagger em http://127.0.0.1:8001/docs***

## Estrutura do projeto

```
download-yt-video/
│── app/
│   ├── main.py               # Arquivo principal da API FastAPI
│   ├── pytube_handler.py      # Lógica de download do YouTube
│── downloads/                 # Pasta onde os vídeos são salvos - gerada automaticamente
│── requirements.txt           # Dependências do projeto
│── README.md                  # Documentação do projeto
```

## Possíveis Erros

***ModuleNotFoundError: No module named 'pytubefix'***
Isso significa que o pytubefix não está instalado. Execute:

```bash
pip install pytubefix
```

***ERROR: Address already in use***
Se a porta 8001 já estiver em uso, tente iniciar o servidor em outra porta:

```bash
uvicorn app.main:app --reload --port 8080
```

## Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests.
***Mantenha o código limpo e organizado!***

## Licença

Este projeto está sob a licença MIT.
```css
Esse README cobre desde a instalação até o uso e solução de problemas. Se precisar de ajustes, me avise!
```