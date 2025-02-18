import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier  
import pickle

# Load the PREPROCESSED data
df = pd.read_csv("../data/processed_fraud_data.csv")  

# Define features (X) and target (y)
X = df.drop("class", axis=1)
y = df["class"]

# Split data (optional, but good practice)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(random_state=42) # Your model
model.fit(X_train, y_train)

# Save the trained model (relative path)
with open("../models/fraud_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved!")