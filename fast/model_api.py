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

    # Check if all columns are present in the input data DataFrame
    missing_columns = set(model.features) - set(input_data_df.columns)

    if missing_columns:
        raise ValueError(f"The following columns are missing from the input data DataFrame: {missing_columns}")

    # Check if the model is trained
    if not model.trained:
        raise ValueError("The model is not trained. Please train the model before making predictions.")

    # Make prediction
    prediction = predict_model(model, input_data_df)['Label'][0]

    # Create an OutputData object with the prediction
    output_data = OutputData(prediction=prediction)

    return output_data


if __name__ == "__main__":
    uvicorn.run(app, host="00.00.0.0", port=8000)
