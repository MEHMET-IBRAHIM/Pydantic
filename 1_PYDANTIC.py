# first problem of pydantic  (TYPE VALIDATION)
def Patient_data(name:str , age:int):
    if type(name) == str and type(age)== int:
        print(name)
        print(age)
        print("update")
    else:    
        raise TypeError("incorrect datatype")
  
Patient_data("ALI",34)


# SECOND PROBLEM (VALIDATION AND CONSTARINS)eg age NOT EQUAL TO NEGATIVE
def Patients_age(age:int):
    if age > 0:
        print("valid")
    else:
        raise ValueError("age is wrong")
Patients_age(5)        





