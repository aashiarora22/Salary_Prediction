from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    years = float(request.form["experience"])
    prediction = model.predict([[years]])[0]
    return render_template("index.html", prediction=round(prediction, 2))

if __name__ == "__main__":
    app.run(debug=True)