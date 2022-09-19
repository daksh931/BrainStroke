# importing the libraries
from flask import Flask,render_template,request
import pickle

#Global variables
app=Flask(__name__)
loaded_model=pickle.load(open('Logistic Model.pkl','rb'))

#user defined routes
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/prediction",methods=['POST'])
def predict():
    gender=request.form['gender']
    age=request.form['age']
    hypertension=request.form['hypertension']
    Heartdisease=request.form['Heart disease']
    EverMarried=request.form['ever married']
    worktype=request.form['age']
    residence=request.form['work type']
    Average_glucose_level=request.form['Average glucose level']
    bmi=request.form['bmi']
    Smoking_status=request.form['Smoking status']
    
    
    prediction=loaded_model.predict([[gender,age, hypertension,Heartdisease,EverMarried,worktype,residence,Average_glucose_level,bmi,Smoking_status]])[0]
    
    if prediction==0:
        prediction=" no Stroke"
    else:
        prediction='stroke'
        
    return render_template("index.html",output_prediction=prediction)


if __name__ =='__main__':
    app.run(debug=True)       


