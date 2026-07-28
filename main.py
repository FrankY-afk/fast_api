from fastapi import FastAPI
import json

app=FastAPI()

def load_data():
    with open('patients.json','r')as f: 
        ans=json.load(f)
    return ans

@app.get("/")
def hello():
    return {'message: patient management system API'}
@app.get("/about")
def about():
    return {'message: a fully functional api systen'}
@app.get('/view')
def view():
    data=load_data()

    return data
@app.get('/patient/{patient_id}')
def view_patient(patient_id:str):
    # load patients
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        return {"error": "Patient not found"}