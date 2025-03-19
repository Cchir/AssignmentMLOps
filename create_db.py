import sqlite3
import pandas as pd
import seaborn as sns
# Load the penguins dataset. It requires package 'seaborn'
penguins = sns.load_dataset("penguins").dropna()
penguins.info()
# Define database name
db_path = "penguins.db"
# Connect to SQLite (creates the database file if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS penguins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    species TEXT,
    island TEXT,
    bill_length_mm REAL,
    bill_depth_mm REAL,
    flipper_length_mm REAL,
    body_mass_g REAL,
    sex TEXT
);
""")

# Insert data
penguins.to_sql("penguins", conn, if_exists="replace", index=False)

# Commit and close connection
conn.commit()
conn.close()

print(f"Database saved as {db_path}")

# Reconnect to database and fetch some data
conn = sqlite3.connect(db_path)
df = pd.read_sql_query("SELECT * FROM penguins LIMIT 5;", conn)
conn.close()

# Display data
print(df)