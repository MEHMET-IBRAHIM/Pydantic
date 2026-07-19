from pydantic import BaseModel

class Myself(BaseModel):
    name:str
    age:int
    religion:str

def me(myself:Myself):
    print(myself.name)
    print(myself.age)
    print(myself.religion)

info={'name':"MUHAMMAD ABDULLAH",'age':21,'religion':'ISLAM'}

Abdullah=Myself(**info)

me(Abdullah) 












