# Ponderada4 - M7 Construção de Dashboard para Visualização de Dados

Autor: Alysson Cordeiro.

## Descrição: 
Este projeto consiste em um dashboard desenvolvido em Streamlit para visualização de dados de predição de COVID-19 na cidade de Toronto. Ele exibe informações sobre casos confirmados (1) e não confirmados (0) e inclui autenticação por meio de login.

## Desenvolvimento:

### Colab:
- Responsável por gerar o Api do modelo, usando a função do Pycaret ``create_api()``.
- Link do Colab: https://colab.research.google.com/drive/1fGh0QMEHhlC0hivOub03WCWFFvTzTu_7?usp=sharing

### Backend:
- Desenvolvido em python e utilizando o framework FastApi.
- O seu propósito é receber as solicitações de previsão e, em seguida, responder a elas com base no modelo criado na fase anterior.

### Frontend:

- Desenvolvido em python e utilizando o framework Stremlit.
- Página de predisão: neste local, o usuário pode inserir os dados para efetuar uma previsão.

### AWS:

O projeto foi executado na nuvem utilizando o serviço EC2 da AWS. Foi usado o o terminal Ubuntu.

## Instalação:

Crie um EC2 na AWS usando Ubuntu e instale os comandos base para o projetos:

```python
sudo apt update
sudo apt upgrade
sudo apt install python3 python3-pip -y
```

Instale o Docker também:

```python
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

```python
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

```

Após finalizar a instalação, clone o repositório que está no Github:

```python
git clone https://github.com/alyssoncastro/ponderada4-m7.git
```

Não esqueça de  instalar as dependências:

```python
pip install fastapi
pip install pycaret
pip install uvicorn
pip install pandas
pip install numpy
pip install pydantic
pip install streamlit
```

Caminhe até o diretório do projeto. Aqui como deram problemas técnico, teremos que rodar por parte, pois não rodou por inteiro. Para mais detalhes leia o meu documento que está em ``cd ponderada4-m7/doc/documentation.md``.

Então, para rodar o API, precisa-se que vá até o diretorio ``cd/ponderada4_m7/fast/`` e aplique o comando:

```python
uvicorn model_api:app --host 0.0.0.0 --port 8000
```
veja o vídeo da API: https://drive.google.com/file/d/17RMqgpOFB9WzU1ysolCUcOPghrqdYbSu/view?usp=sharing

Então, para rodar o Streamlit, precisa-se que vá até o diretorio ``cd/ponderada4_m7/fast/Interface`` e aplique o comando:

```python
streamlit run streamlit.py
```

veja o vídeo do Dashboard: https://drive.google.com/file/d/1TsLaCUHCMo6EU0Czv-myeCHvCb2VH-Z8/view?usp=sharing

### LEIA A DOCUMENTAÇÃO!
