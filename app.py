from flask import Flask,request,jsonify
import pickle

model_file = open("regmodel.pkl", "rb")
model = pickle.load(model_file)

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to flask"

@app.route("/predict",methods=["GET","POST"])
def hi():
    if request.method == "GET":
        return "Boston house pricing prediction"
    else:
        price = request.get_json()
        

        CRIM = price["CRIM"]
        ZN = price["ZN"]
        INDUS = price["INDUS"]
        CHAS = price["CHAS"]
        NOX = price["NOX"]
        RM = price["RM"]
        AGE = price["AGE"]
        DIS = price["DIS"]
        RAD = price["RAD"]
        TAX = price["TAX"]
        PTRATIO = price["PTRATIO"]
        B = price["B"]
        LSTAT = price["LSTAT"]

        input_data = [
    price["CRIM"], price["ZN"], price["INDUS"], price["CHAS"], price["NOX"],
    price["RM"], price["AGE"], price["DIS"], price["RAD"], price["TAX"],
    price["PTRATIO"], price["B"], price["LSTAT"]
]

    result = model.predict([input_data])

    return jsonify({"predicted_price": result[0]})