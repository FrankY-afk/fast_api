

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

from pydantic import BaseModel,EmailStr,AnyURL,Field
from typing import list,Optional

class patient(BaseModel):
    name:str
    email:EmailStr
    linkedin_url:AnyURL
    age:int =Field(gt=0,lt=120)
    weight:float=Field(gt=0)
    married:bool
    allergies:optional[list[str]]=None 
    contact_detail:dict[str,str]


patient_inf0={'name':'Chirag','age':21,'weight':62.0,'married':False,'allergies':'dust','contact_details':{'email':'abc@gmail.com','phone':'1234567'}}
patient1=patient(**patient_inf0)