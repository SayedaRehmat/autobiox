import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load the training dataset (must be in the same folder)
df = pd.read_csv("AutoBioX_Training_Data.csv")

# Split data
X = df.drop("Subtype", axis=1)
y = df["Subtype"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save model to file
joblib.dump(model, "autobiox_model.pkl")
print("✅ Model saved as autobiox_model.pkl")
