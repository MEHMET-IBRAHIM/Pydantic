#nested models
from pydantic import BaseModel
from typing import Dict


class Patient_address(BaseModel):
    House_no:int
    city:str
    state:str
    pin:str


class Patient(BaseModel):
    name :str
    gender:str
    age:int
    address:Patient_address


address_dcit={'city':'islamabad','state':'Pakistan','pin':'2468','House_no':'123'}
address1=Patient_address(**address_dcit)

patient_dict={'name':'MUHAMMAD ABDULLAH','gender':'M','age':'21','address':address1}

patient1=Patient(**patient_dict)

print(patient1)
print(patient1.address.pin)