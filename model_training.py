import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

#  Step 1: Correct file path (from src/ to data/)
file_path = os.path.join("..", "data", "bhandara_merged.csv")

#  Step 2: Load CSV safely
try:
    df = pd.read_csv(file_path)
    print("📂 Data loaded successfully.")
except FileNotFoundError:
    print(f"❌ File not found: {file_path}")
    exit()


#  Step 3: Check available columns
print("🧪 Available columns:", df.columns.tolist())

#  Step 4: Make sure required columns exist
required_columns = ['District', 'actual', 'normal', 'deviation', 'currentlevel']
missing = [col for col in required_columns if col not in df.columns]
if missing:
    print(f"❌ Missing columns in CSV: {missing}")
    exit()

#  Step 5: Filter for Bhandara district
df['District'] = df['District'].str.lower().str.strip()
df = df[df['District'] == 'bhandara']

#  Step 6: Drop missing values
df = df.dropna(subset=['actual', 'normal', 'deviation', 'currentlevel'])

#  Step 7: Define features and target
X = df[['actual', 'normal', 'deviation']]
y = df['currentlevel']

#  Step 8: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#  Step 9: Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 10: Save model in /models/ folder
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/groundwater_model.pkl")
print(" Model trained and saved as models/groundwater_model.pkl")





