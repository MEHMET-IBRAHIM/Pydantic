#----topics------
#field validator

from pydantic import BaseModel,Field,AnyUrl,EmailStr,field_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: str
    age: int
    email:EmailStr
    weight:float
    married:str
    allergies:Optional[List[str]]=None
    contact_details:Dict[str,str]
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=['hdfc.com','icici.com']
        domain_name=value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    

    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    @field_validator('age')#,mode='after')
    @classmethod
    def validate_age(cls,value):
        if 0<value<100:
            return value
        else:
            raise ValueError('AGE IS JUST A NUMBER 😂')
        



def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print('----update----')

patient_info={'name':"MUHAMMAD Abdullah",'age':'99','email':'abc@icici.com','weight':78.9,'married':'IN-SHA-ALLAH','contact_details':{'phone_no':'03295116182','house':'margalla'}}
patient1=Patient(**patient_info)
update_patient_data(patient1)




