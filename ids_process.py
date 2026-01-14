import joblib
import numpy as np
from alert import send_alert

model = joblib.load("models/random_forest.pkl")

def detect(packet_features):
    prediction = model.predict([packet_features])
    if prediction[0] == 1:
        send_alert("Malicious Activity Detected")

