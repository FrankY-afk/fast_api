from pydantic_demo import BaseModel

class address(BaseModel):
    city:str
    state:str
    pin:str

class patient:
    name:str
    gender:str
    age:int
    address:str

address_dict={'city':'gurgaon','state':'haryana','pin':'122001'}

address1=address(**address_dict)
patient_dict={'name':'chirag','gender':'male','age':21,'address':address1}

patient1=patient(patient_dict)

print(patient)
