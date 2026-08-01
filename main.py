from fastapi.responses import JSONResponse
from fastapi import FastAPI, Path, HTTPException, Query
import json
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal

app = FastAPI()

class patient(BaseModel):
    id:Annotated[str,Field(...,description='id of the patient',examples=['p001'])]
    name:Annotated[str,Field(...,description='name of the patient',examples=['john'])]
    city:Annotated[str,Field(...,description='name of the city')]
    age:Annotated[int,Field(...,gt=0,lt=120,description='what is the age of patient')]
    gender:Annotated[Literal['male','female','others'],Field(...,description='gender of the patient')]
    height:Annotated[float,Field(...,gt=0,description='height of the ')]
    weight:Annotated[float,Field(...,gt=0,description='weight of the pattetnt')]

    @computed_field
    @property
    def bmi(self) ->float:
        bmi=self.weight/self.height**2
        return bmi
    @computed_field
    @property
    def verdict(self)->float:
        if(self.bmi<18.5):
            return 'underweight'
        elif(self.bmi <30):
            return 'normal'
        else:
            return 'obese'
def load_data():
    with open('patients.json', 'r') as f:
        ans = json.load(f)
    return ans
def save_data():
    with open('patients.json', 'w') as f:
        json.dump(f)



@app.get("/")
def hello():
    return {"message": "Patient Management System API"}


@app.get("/about")
def about():
    return {"message": "A fully functional API system"}


@app.get('/view')
def view():
    data = load_data()
    return data


@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description="Patient ID")):
    data = load_data()

    if patient_id in data:
        return data[patient_id]

    raise HTTPException(status_code=404, detail="PATIENT NOT FOUND")


@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., description="Sort on the basis of height, weight or bmi"),
    order: str = Query("asc", description="Sort in asc or desc")
):
    view_fields = ['height', 'weight', 'bmi']

    if sort_by not in view_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sort field. Allowed values are {view_fields}"
        )

    if order not in ['asc', 'desc']:
        raise HTTPException(
            status_code=400,
            detail="Order should be either 'asc' or 'desc'"
        )

    data = load_data()

    sort_order = True if order == "desc" else False

    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=sort_order
    )

    return sorted_data

@app.post('/create')
def create_patient(patient:patient):
    # load data
    data=load_data()
    # check if it is also present
    if(patient.id in data):
        raise HTTPException(status_code=400,detail='patient alr present')
    # create new
    data['new_patient_id']=patient.model_dump(exclude='id')
    # converting pydantic data to python
    save_data()
    # saved data
    return JSONResponse(
    status_code=201,
    content={"message": "Patient created successfully"}
)