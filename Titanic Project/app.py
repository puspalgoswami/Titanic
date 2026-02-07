from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

logistic_model = joblib.load("logistic_model.pkl")
rf_model = joblib.load("rf_model.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = ""

    form_data = {
        "pclass": "",
        "sex": "",
        "age": "",
        "sibsp": "",
        "parch": "",
        "fare": "",
        "model": "logistic"
    }

    if request.method == "POST":

        try:
            pclass = int(request.form["pclass"])
            sex = int(request.form["sex"])
            age = float(request.form["age"])
            sibsp = int(request.form["sibsp"])
            parch = int(request.form["parch"])
            fare = float(request.form["fare"])
            model_type = request.form["model"]

            form_data["pclass"] = pclass
            form_data["sex"] = sex
            form_data["age"] = age
            form_data["sibsp"] = sibsp
            form_data["parch"] = parch
            form_data["fare"] = fare
            form_data["model"] = model_type

            data = np.array([
                [pclass, sex, age, sibsp, parch, fare]
            ])

            if model_type == "logistic":
                result = logistic_model.predict(data)[0]
            else:
                result = rf_model.predict(data)[0]

            if result == 1:
                prediction = "✅ Passenger Survived"
            else:
                prediction = "❌ Passenger Did Not Survive"

        except Exception as e:
            prediction = "⚠️ Error: Please check your inputs"
            print("Error:", e)

    return render_template(
        "index.html",
        prediction=prediction,
        form_data=form_data
    )


if __name__ == "__main__":
    app.run(debug=True)