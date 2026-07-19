#------TOPICS------
#pydabtic , Base model
#Type Validation {Optional}
#Data Validation {EmailStr} =CUSTOM DATA TYPE
#Field function =Custom data type Validation



from pydantic import BaseModel , EmailStr,AnyUrl,Field #CUSTOM DATA TYPE
from typing import List ,Dict ,Optional,Annotated #Type Validation

class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title="NAME OF THE PATIENT",description="Given name less than 50 chararcters")] #Data validation so that no one will give u gabrish data
    age:int =Field(gt=0,lt=120)
    weight:Annotated [Optional[float],Field(default=None,gt=0,strict=True)]
    married:Annotated [bool,Field(default=None,description="is the patient married or not")]
    diseases:Optional[List[str]] =Field(max_length=5)
    contact_details:Dict[str,str]
    email:EmailStr
    

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print('--inserted--')

patient_info={'email':'ABC@gamil.com','name':'MUHAMMAD ABDULLAH','age':"30", 'weight':75.9,'diseases':['pollen','dust'],'contact_details':{'email':'ABDULLAH@gmail.com}','phone':'03295116137'},'married':'NO'}
              
patient1=Patient(**patient_info)    
insert_patient_data(patient1)







#can call multiple functions u need to just change name