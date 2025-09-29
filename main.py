from fastapi import FastAPI
import joblib

# Load trained model
model = joblib.load("iris_model.pkl")

# Create API
app = FastAPI()

@app.post("/predict")
def predict(features: list):
    prediction = model.predict([features])
    return {"prediction": int(prediction[0])}
