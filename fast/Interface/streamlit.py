import streamlit as st
import requests
import matplotlib.pyplot as plt

# Título do aplicativo
st.title('Classificação do Modelo COVID-19 com Base na API')

# Fazer uma solicitação à API (substitua a URL pela URL real da sua API)
api_url = "http://54.211.0.252:8000/predict"  # Substitua pela URL da sua API
data = {
    "feature1": 1,
    "feature2": 2,
}

response = requests.post(api_url, json=data)

# Verificar se a solicitação à API foi bem-sucedida
if response.status_code == 200:
    api_data = response.json()
    prediction = api_data.get("prediction")

    # Criar um gráfico com base na classificação
    fig, ax = plt.subplots()
    labels = ['Positivo', 'Negativo']
    sizes = [prediction, 1 - prediction]
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('Classificação do Modelo COVID-19')

    # Exibir o gráfico no aplicativo Streamlit
    st.pyplot(fig)
else:
    st.error('Não foi possível obter a classificação do modelo a partir da API.')
