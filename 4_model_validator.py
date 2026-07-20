#model_validator


from pydantic import BaseModel,Field,AnyUrl,EmailStr,field_validator , model_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: str
    age: int
    email:EmailStr
    weight:float
    married:str
    allergies:Optional[List[str]]=None
    contact_details:Dict[str,str]



    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency'not in model.contact_details:
            raise ValueError('PATIENTS older than 60 must have an emergency contact')
        return model
    

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print('----update----')

patient_info={'name':"MUHAMMAD Abdullah",'age':'99','email':'abc@icici.com','weight':78.9,'married':'IN-SHA-ALLAH','contact_details':{'phone_no':'03295116182','house':'margalla','emergency':'676879'}}
patient1=Patient(**patient_info)
update_patient_data(patient1)

