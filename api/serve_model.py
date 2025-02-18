from flask import Flask, request, jsonify
import pickle
import pandas as pd
from flask_logging import Logging
import logging

app = Flask(__name__)
Logging(app)

# Load the trained model
with open("../models/fraud_model.pkl", "rb") as f:  # Relative path correction
    model = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # IMPORTANT: No preprocessing needed here because it's ALREADY DONE
        # The data received should be in the exact format the model was trained on
        df = pd.DataFrame([data])  # Direct conversion to DataFrame

        prediction = model.predict(df)[0]
        app.logger.info(f"Incoming request: {data}")
        app.logger.info(f"Prediction: {prediction}")
        return jsonify({"prediction": int(prediction)})

    except Exception as e:
        app.logger.error(f"Error during prediction: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')