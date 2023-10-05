# -*- coding: utf-8 -*-

import pandas as pd
from pycaret.classification import load_model, predict_model
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

# Create the app
app = FastAPI()

# Load trained Pipeline
model = load_model("model_api")

# Create input/output pydantic models
class InputData(BaseModel):
    Outbreak_Associated: str
    Neighbourhood_Name: str
    FSA: str
    Source_of_Infection: str
    Episode_Date: str
    Client_Gender: str
    Outcome: str
    Currently_Hospitalized: int
    Currently_in_ICU: int
    Currently_Intubated: int

class OutputData(BaseModel):
    prediction: int

# Define predict function
@app.post("/predict", response_model=OutputData)
def predict(data: InputData):
    data_dict = data.dict()
    data_df = pd.DataFrame([data_dict])
    predictions = predict_model(model, data=data_df)
    return {"prediction": predictions["Label"].iloc[0]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)