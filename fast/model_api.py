# -*- coding: utf-8 -*-

import pandas as pd
from pycaret.classification import load_model, predict_model
from fastapi import FastAPI
import uvicorn
from pydantic import create_model

# Cria a aplicação
app = FastAPI()

# Carrega o modelo treinado
model = load_model("model_api")

# Cria os modelos pydantic de entrada e saída
cliente_dados = create_model(
    "model_api_input",
    client_id=13416,
    bairro="Mount Olive-Silverstone-Jamestown",
    FSA="M9V",
    fonte_de_infecção="Comunidade",
    data_do_episódio="2020-05-04",
    sexo_do_cliente="1",
    resultado="1",
    hospitalizado_atualmente=0,
    internado_em_uti_atualmente=0,
    intubado_atualmente=0,
    hospitalizado_alguma_vez=0,
    internado_em_uti_alguma_vez=0,
    intubado_alguma_vez=0,
)
predication = create_model("model_api_output", previsão=1)


# Define a função de previsão
@app.post("/predict", response_model=predication)
def predict(cliente_dados: cliente_dados):
    cliente_dados = pd.DataFrame([cliente_dados.dict()])
    previsões = predict_model(model, data=cliente_dados)
    return {"predication": previsões["predication_label"].iloc[0]}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)