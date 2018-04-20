from flask import Flask, request, jsonify
from flask_api import status
import settings
import emailVerifier
import distance_calc
import retirement
import tip_calc
import bmi

app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({"application": "Team 6 API"})

@app.route('/bmi')
def bmiCalculator():
    args = request.args.to_dict()

    if ("feet" not in args):
        return "Expected parameter 'feet'.", status.HTTP_400_BAD_REQUEST

    feet = args["feet"]

    if not args["feet"].isnumeric():
        return "Parameter 'feet' must be an integer.", status.HTTP_400_BAD_REQUEST

    if ("inches" not in args):
        return "Expected parameter 'inches'.", status.HTTP_400_BAD_REQUEST

    inches = args["inches"]

    if not args["inches"].isnumeric():
        return "Parameter 'inches' must be an integer.", status.HTTP_400_BAD_REQUEST

    if ("weight" not in args):
        return "Expected parameter 'weight'.", status.HTTP_400_BAD_REQUEST

    weight = args["weight"]

    if not (args["weight"].replace(".", "", 1)).isnumeric():
        return "Parameter 'weight' must be a float.", status.HTTP_400_BAD_REQUEST
        
    feet = int(feet)
    inches = int(inches)
    weight = float(weight)

    return jsonify({'bmi': bmi.calcBmi(feet, inches, weight)})

@app.route('/retire')
def retire():
    args = request.args.to_dict()

    # age
    if ("age" not in args):
        return "Expected parameter 'age'.", status.HTTP_400_BAD_REQUEST

    age = args["age"]

    if not age.isnumeric():
        return "Parameter 'age' must be an integer.", status.HTTP_400_BAD_REQUEST

    # salary
    if ("salary" not in args):
        return "Expected parameter 'salary'.", status.HTTP_400_BAD_REQUEST

    salary = args["salary"]

    if not (salary.replace(".", "", 1)).isnumeric():
        return "Parameter 'salary' must be a float.", status.HTTP_400_BAD_REQUEST

    # saved
    if ("saved" not in args):
        return "Expected parameter 'saved'.", status.HTTP_400_BAD_REQUEST

    saved = args["saved"]

    if not (saved.replace(".", "", 1)).isnumeric():
        return "Parameter 'saved' must be a float.", status.HTTP_400_BAD_REQUEST

    # goal
    if ("goal" not in args):
        return "Expected parameter 'goal'.", status.HTTP_400_BAD_REQUEST

    goal = args["goal"]

    if not goal.isnumeric():
        return "Parameter 'goal' must be an integer.", status.HTTP_400_BAD_REQUEST

    age = int(age)
    salary = float(salary)
    saved = float(saved)
    goal = int(goal)

    result = retirement.findRetirementAge(age, salary, saved, goal)
    if type(result) is bool or result >= 100:
        return jsonify({"goalMet": False, "age": None})
    else:
        return jsonify({"goalMet": True, "age": result})

@app.route('/distance')
def distance():
    args = request.args.to_dict()

    # x1
    if ("x1" not in args):
        return "Expected parameter 'x1'.", status.HTTP_400_BAD_REQUEST

    x1 = args["x1"]

    if not (x1.replace(".", "", 1)).isnumeric():
        return "Parameter 'x1' must be a float.", status.HTTP_400_BAD_REQUEST

    # y1
    if ("y1" not in args):
        return "Expected parameter 'y1'.", status.HTTP_400_BAD_REQUEST

    y1 = args["y1"]

    if not (y1.replace(".", "", 1)).isnumeric():
        return "Parameter 'y1' must be a float.", status.HTTP_400_BAD_REQUEST

    # x2
    if ("x2" not in args):
        return "Expected parameter 'x2'.", status.HTTP_400_BAD_REQUEST

    x2 = args["x2"]

    if not (x2.replace(".", "", 1)).isnumeric():
        return "Parameter 'x2' must be a float.", status.HTTP_400_BAD_REQUEST

    # y2
    if ("y2" not in args):
        return "Expected parameter 'y2'.", status.HTTP_400_BAD_REQUEST

    y2 = args["y2"]

    if not (y2.replace(".", "", 1)).isnumeric():
        return "Parameter 'y2' must be a float.", status.HTTP_400_BAD_REQUEST

    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)

    distance = distance_calc.calculateDistance(x1, y1, x2, y2)
    return (jsonify({'distance': distance}))

@app.route('/email')
def email():
    args = request.args.to_dict()

    if ("email" not in args):
        return "Expected parameter 'email'.", status.HTTP_400_BAD_REQUEST

    email = args["email"]

    return jsonify({"emailValid": emailVerifier.verifyEmail(email)})

@app.route('/tip')
def tip():
    args = request.args.to_dict()

    # subtotal
    if ("subtotal" not in args):
        return "Expected parameter 'subtotal'.", status.HTTP_400_BAD_REQUEST

    subtotal = args["subtotal"]

    if not (subtotal.replace('.','',1)).isnumeric():
        return "Parameter 'subtotal' must be a float.", status.HTTP_400_BAD_REQUEST

    subtotal = float(subtotal)

    # subtotal
    if ("partySize" not in args):
        return "Expected parameter 'partySize'.", status.HTTP_400_BAD_REQUEST

    partySize = args["partySize"]

    if not (partySize.replace('.','',1)).isnumeric():
        return "Parameter 'partySize' must be an integer.", status.HTTP_400_BAD_REQUEST

    partySize = int(partySize)

    dues = tip_calc.calculateTip(subtotal, partySize)

    return jsonify(dues)

def main():
    app.run(port=settings.FLASK_PORT, debug=settings.FLASK_DEBUG)