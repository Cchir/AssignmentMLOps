import os
import joblib
import requests
import pandas as pd

# Load trained model
model_path = "penguin_classifier_model.pkl"
clf = joblib.load(model_path)

# API endpoint
api_url = "http://130.225.39.127:8000/new_penguin/"

try:
    # Fetch new penguin data
    response = requests.get(api_url, timeout=10)
    response.raise_for_status()
    penguin_data = response.json()
    print("Received new penguin data:", penguin_data)

    # Convert to DataFrame
    df_new = pd.DataFrame([penguin_data])

    # Select relevant features
    features = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
    df_new = df_new[features]

    # Make prediction
    prediction = clf.predict(df_new)[0]

    # Ensure 'predictions/' and 'docs/' directories exist
    os.makedirs("predictions", exist_ok=True)
    os.makedirs("docs", exist_ok=True)

    # Save prediction to text file
    result_path = "predictions/latest_prediction.txt"
    with open(result_path, "w") as file:
        file.write(prediction)

    print(f"Prediction saved: {prediction}")

    # Create HTML output for GitHub Pages
    html_path = "docs/index.html"
    with open(html_path, "w") as file:
        file.write(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Latest Penguin Prediction</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin: 50px;
                }}
                h1 {{
                    color: #2c3e50;
                }}
                #prediction {{
                    font-size: 24px;
                    font-weight: bold;
                    color: #27ae60;
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>

            <h1>Penguin Species Prediction</h1>
            <p>Every day at 7:30 AM, we analyze a new penguin found in New York!</p>

            <h2>Latest Prediction:</h2>
            <p id="prediction">{prediction}</p>

        </body>
        </html>
        """)

    print(f"Prediction updated on GitHub Pages.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    exit(1)  # Exit script gracefully

