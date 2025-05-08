import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# Load dataset
df = pd.read_csv(r'crop_data.csv')

# Encode categorical features
df = pd.get_dummies(df, columns=['Crop_Type', 'Fertilizer_Used'], drop_first=False)


# Features and target
X = df.drop('Yield', axis=1)
y = df['Yield']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Store expected feature names for Flask use
model.feature_names_in_ = X.columns

# Save model
os.makedirs('models', exist_ok=True)
joblib.dump(model, 'yield_predictor.pkl')

print("✅ Model trained and saved as yield_predictor.pkl")

print("Model expects these features:")
print(list(X.columns))

