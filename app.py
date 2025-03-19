import seaborn as sns
import pandas as pd
import sqlite3
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
# Connect to SQLite database
db_path = "data/penguins.db"
conn = sqlite3.connect(db_path)

# Read data from the database
df = pd.read_sql_query("SELECT * FROM penguins", conn)

# Close connection
conn.close()

# Selecting relevant features
features = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
target = 'species'

X = df[features]
y = df[target]


# Split dataset into training (80%) and testing (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Initialize model
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
clf.fit(X_train, y_train)

# Predict on the test set
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")


# Save the trained model
model_path = "penguin_classifier_model.pkl"
joblib.dump(clf, model_path)

print(f"Model saved as {model_path}")
