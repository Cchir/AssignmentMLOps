import joblib
import requests
import pandas as pd

# Load trained model
model_path = "penguin_classifier_model.pkl"
clf = joblib.load(model_path)

# API endpoint
api_url = "http://130.225.39.127:8000/new_penguin/"

# Fetch new penguin data
response = requests.get(api_url)
if response.status_code == 200:
    penguin_data = response.json()
    print("Received new penguin data:", penguin_data)

    # Convert to DataFrame
    df_new = pd.DataFrame([penguin_data])

    # Select relevant features
    features = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
    df_new = df_new[features]

    # Make prediction
    prediction = clf.predict(df_new)[0]

    # Save prediction
    result_path = "predictions/latest_prediction.txt"
    with open(result_path, "w") as file:
        file.write(f"New Penguin Species: {prediction}\n")
    
    print(f"Prediction saved: {prediction}")

else:
    print(f"Failed to fetch new data. Status Code: {response.status_code}")
