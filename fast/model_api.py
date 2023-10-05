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
@app.post("/predict")
async def predict(input_data: InputData):
    # Convert dict to DataFrame with index
    input_data_df = pd.DataFrame(input_data.dict(), index=[0])
    # Get the list of features from the model
    features = model.get_features()
    # Check if all features are present in the input data DataFrame
    missing_features = set(features) - set(input_data_df.columns)
    if missing_features:
        raise ValueError(f"The following features are missing from the input data DataFrame: {missing_features}")
    # Make prediction
    prediction = predict_model(model, input_data_df)['Label'][0]
    # Create an OutputData object with the prediction
    output_data = OutputData(prediction=prediction)
    return output_data


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
