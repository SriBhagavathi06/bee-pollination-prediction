# app.py
from flask import Flask, render_template, request, redirect
from utils.database import insert_data, get_all_data
from utils.ml_utils import get_prediction

app = Flask(__name__)

@app.route("/")
def index():
    data = get_all_data()
    return render_template("index.html", data=data)

@app.route("/add", methods=["GET", "POST"])
def add_data():
    if request.method == "POST":
        feature1 = float(request.form["feature1"])
        feature2 = float(request.form["feature2"])
        pollination_success = int(request.form["pollination_success"])
        
        # Add data to DB
        insert_data(feature1, feature2, pollination_success)
        return redirect("/")
    
    return render_template("add_data.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    prediction_text = None
    if request.method == "POST":
        feature1 = float(request.form["feature1"])
        feature2 = float(request.form["feature2"])
        
        # Prepare input data
        input_data = [feature1, feature2]
        
        # Get prediction
        result = get_prediction(input_data)
        
        prediction_text = "Pollination Successful 🐝✅" if result == 1 else "Pollination Unsuccessful ❌"
    
    return render_template("predict.html", prediction=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
