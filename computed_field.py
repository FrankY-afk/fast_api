from pydantic_demo import BaseModel,EmailStr,computed_field
from typing import list,Dict

class patient(BaseModel):
    name:str
    email:str
    age:int
    weight:float
    height:float
    married:bool
    allergies:list[str]
    contact_detils=Dict[str,str]
    @computed_field
    @property
    def calculate_bmi(self) ->float:
        bmi= round(self.weight + (s.height**2),2)
        return bmi

    def update_patient_id(name: str, age: int):
        if age < 0:
            raise ValueError("Age can't be less than 0")

        if isinstance(name, str) and isinstance(age, int):
            print(name)
            print(age)
            print('BMI',patient.calculate_bmi)
            print("updated")
        else:
            raise TypeError("Incorrect data type")
    
    