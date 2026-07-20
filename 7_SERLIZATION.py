#Importing,debugging,logging


from pydantic import BaseModel

class Adderess(BaseModel):
    city: str
    state:str
    pin:int


class Patient(BaseModel):
    name :str
    age:int
    gender:str
    address:Adderess



address_dcit={'city':'islamabad','state':'Pakistan','pin':'2468','House_no':'123'}
address1=Adderess(**address_dcit)

patient_dict={'name':'MUHAMMAD ABDULLAH','gender':'M','age':'21','address':address1}

patient1=Patient(**patient_dict)

print(patient1)
print(patient1.address.pin)


patient1.model_dump()  # convert pydantic model object into python doctionary
temp=patient1.model_dump(include=['name']) #allow specific vaiables
print(temp)
print(type(temp))
print("----------------DONE-----------------")

patient1.model_dump_json()  # convert pydantic model object into python doctionary
temp=patient1.model_dump_json()
print(temp)
print(type(temp))

#exclude unset
