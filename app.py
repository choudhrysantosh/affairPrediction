from flask import Flask,render_template,request
import pickle



app = Flask(__name__)
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    age = float(request.form['age'])
    no_of_years_married = float(request.form['no_of_years_married'])
    children = float(request.form['children'])
    rate = float(request.form['rate'])
    religious = float(request.form['religious'])
    education = float(request.form['education'])
    occupation = float(request.form['occupation'])
    husband_occupation = float(request.form['husband_occupation'])
    print([rate,age,children,religious,education,occupation,husband_occupation])

    model = pickle.load(open(r'modelForPrediction.pkl', 'rb'))
    scaler = pickle.load(open(r'sandardScalar.pkl', 'rb'))
    prediction = model.predict(scaler.transform([[rate,age,children,religious,education,occupation,husband_occupation]]))
    output = prediction[0]
    print(output)
    if output == 1:
        return render_template('index.html', prediction_text="WOMEN IS INTRESTED IN EXTRAMARITAL AFFAIR")
    else:
        return render_template('index.html', prediction_text="WOMEN IS NOT INTRESTED IN EXTRAMARITAL AFFAIR")

if __name__=="__main__":
    app.run(debug=True)