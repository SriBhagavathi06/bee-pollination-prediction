# models/logistic_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load and preprocess data
def load_data(file_path):
    data = pd.read_csv(file_path)
    X = data.drop("pollination_success", axis=1)
    y = data["pollination_success"]
    return X, y

# Train logistic regression model
def train_model(file_path):
    X, y = load_data(file_path)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")
    
    return model

# Predict pollination success
def predict_pollination(model, input_data):
    prediction = model.predict([input_data])
    return prediction[0]
