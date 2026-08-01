from pydantic_demo import BaseModel, EmailStr, AnyUrl, Field, field_validator,model_validator
from typing import Optional, Annotated


def update_patient_id(name: str, age: int):
    if age < 0:
        raise ValueError("Age can't be less than 0")

    if isinstance(name, str) and isinstance(age, int):
        print(name)
        print(age)
        print("updated")
    else:
        raise TypeError("Incorrect data type")


class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50)]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: float = Field(gt=0)
    married: bool
    allergies: Optional[list[str]] = None
    contact_detail: dict[str, str]

    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        valid_domains=['hdfc.com','icic.com']
        domain_name=value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError(value=400)
        return value

    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()

    @model_validator(mode='after')
    def validate_emergency(cls,model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError('emergency contact is not present')
        return model