# -*- coding: utf-8 -*-

import pandas as pd
from pycaret.classification import load_model, predict_model
from fastapi import FastAPI
import uvicorn
from pydantic import create_model

# Create the app
app = FastAPI()

# Load trained Pipeline
model = load_model("model_api")

# Create input/output pydantic models
input_model = create_model("model_api_input", **{'Unnamed: 0': 13416, 'Neighbourhood Name': 'Mount Olive-Silverstone-Jamestown', 'FSA': 'M9V', 'Source of Infection': 'Community', 'Episode Date': '2020-05-04', 'Client Gender': '1', 'Outcome': '1', 'Currently Hospitalized': 0, 'Currently in ICU': 0, 'Currently Intubated': 0, 'Ever Hospitalized': 0, 'Ever in ICU': 0, 'Ever Intubated': 0})
output_model = create_model("model_api_output", prediction=1)


# Define predict function
@app.post("/predict", response_model=output_model)
def predict(data: input_model):
    data = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=data)
    return {"prediction": predictions["prediction_label"].iloc[0]}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)