#Computed Field
from pydantic import BaseModel,Field,AnyUrl,EmailStr,field_validator , model_validator,computed_field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: str
    age: int
    email:EmailStr
    weight:float
    height:float
    married:str
    allergies:Optional[List[str]]=None
    contact_details:Dict[str,str]

    @computed_field
    @property
    def calculate_bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi



def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print('----update----')
    print('BMI',patient.calculate_bmi)

patient_info={'name':"MUHAMMAD Abdullah",'age':'99','email':'abc@gmail.com','weight':"78.9",'height':'179','married':'IN-SHA-ALLAH','contact_details':{'phone_no':'03295116182','house':'margalla','emergency':'676879'}}
patient1=Patient(**patient_info)
update_patient_data(patient1)

