

def update_patient_id(name:str,age:int):
    if age<0:
        raise ValueError('age cant be less than 0')
    if type(name)==str and type(age)==int:
        print(name)
        print(age)
        print('updated')
    else:
        raise TypeError('incorrect data type')
def insert_patient_id(name:str,age:int):
    if type(name)==str and type(age)==int:
        print(patient.name)
        print(patient,age)
        print(age)
        print('insrted into database')
    else:
        raise TypeError('incorrect data type')

insert_patient_id('chirag',21)

from pydantic import BaseModel

class patient(BaseModel):
    name:str
    age:int

patient_inf0={'name':'Chirag','age':21}
patient1=patient(**patient_inf0)