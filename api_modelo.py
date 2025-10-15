from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import uvicorn

class WaterData(BaseModel):
    ph: float
    Hardness: float
    Solids: float
    Chloramines: float
    Sulfate: float
    Conductivity: float
    Organic_carbon: float
    Trihalomethanes: float
    Turbidity: float

app = FastAPI(title="API de Previsão de Potabilidade da Água")

@app.on_event("startup")
def treinar_modelo():
    global model, feature_columns

    df = pd.read_csv("water_potability_augmented.csv")

    feature_columns = [
        'ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate',
        'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity'
    ]
    X = df[feature_columns]
    y = df['Potability']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    acc = accuracy_score(y_test, model.predict(X_test)) * 100
    print(f"✅ Modelo Random Forest treinado! Acurácia de teste: {acc:.2f}%")

@app.post("/predict")
def predict(data: WaterData):
    input_data = pd.DataFrame([data.dict()])
    prediction = model.predict(input_data)[0]
    return {"Potability": int(prediction)}

if __name__ == "__main__":
    uvicorn.run("api_modelo:app", host="0.0.0.0", port=8000, reload=True)
