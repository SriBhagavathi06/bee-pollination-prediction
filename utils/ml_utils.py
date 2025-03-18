# utils/ml_utils.py
import os
from models.logistic_model import train_model, predict_pollination
from config import CSV_FILE

# Load and train the model
def get_model():
    model = train_model(CSV_FILE)
    return model

# Get prediction based on input data
def get_prediction(input_data):
    model = get_model()
    result = predict_pollination(model, input_data)
    return result
