from flask import Flask
from flask import request
import pickle

app=Flask(__name__)

@app.route("/", methods=["GET"])# we can also mention the method explicitly
def ping():
    return "<H1>Loan Approval Application</H1>"

model_pickle=open("classifier.pkl", "rb")
clf=pickle.load(model_pickle)

@app.route("/predict", methods=["POST"])# It is a post request as user needs to input data to get output 
def predictions(): #and it expects input in the form of json i.e key value pair
    loan_req= request.get_json()#Correction made added parenthesis

    if loan_req["Gender"]=="Male":
        Gender=0
    else:
        Gender=1

    if loan_req["Married"]=="Unmarried":
        Married=0
    else:
        Married=1

    ApplicantIncome=loan_req["ApplicantIncome"]
    LoanAmount=loan_req["LoanAmount"]
    Credit_History=loan_req["Credit_History"]

    result=clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

    if result==0:
        prediction="Not Approved"
    else:
        prediction="Approved"

    return{"Loan Approval Status" : prediction} #key value pair as in dictionary returned
    
