from flask import Flask, render_template, request
import pandas as pd
import joblib
from recommendations import recommend_actions

app = Flask(__name__)

# Load model
model = joblib.load("models/yield_predictor.pkl")

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    suggestions = []

    if request.method == 'POST':
        try:
            rainfall = float(request.form['rainfall'])
            temperature = float(request.form['temperature'])
            humidity = float(request.form['humidity'])
            soil_ph = float(request.form['soil_ph'])
            crop = request.form['crop']
            fertilizer = request.form['fertilizer']

            # Prepare input
            input_data = {
                'Temperature': temperature,
                'Rainfall': rainfall,
                'Humidity': humidity,
                'Soil_pH': soil_ph
            }

            # Encode categorical fields if model expects them
            for col in model.feature_names_in_:
                if col.startswith('Crop_Type_') and f'Crop_Type_{crop}' == col:
                    input_data[col] = 1
                elif col.startswith('Fertilizer_Used_') and f'Fertilizer_Used_{fertilizer}' == col:
                    input_data[col] = 1
                elif col not in input_data:
                    input_data[col] = 0

            df = pd.DataFrame([input_data])
            prediction = round(model.predict(df)[0], 2)

            suggestions = recommend_actions(rainfall, temperature, humidity)

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template("index.html", prediction=prediction, suggestions=suggestions)

if __name__ == '__main__':
    app.run(debug=True)
