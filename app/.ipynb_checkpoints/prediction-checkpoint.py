import joblib
import os
import pandas as pd

# Base project directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Load model and preprocessor
model = joblib.load(os.path.join(BASE_DIR, "models", "best_model_small.pkl"))
preprocessor = joblib.load(os.path.join(BASE_DIR, "models", "preprocessor_small.pkl"))


def predict_employee(data):
    df = pd.DataFrame([data])

    X = preprocessor.transform(df)

    prediction = model.predict(X)[0]
    probability = model.predict_proba(X)[0][1]

    return prediction, probability