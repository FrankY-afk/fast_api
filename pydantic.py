def insert_patient_id(name:str,age:int):
    if type(name)==str and type(age)==int:
        print(name)
        print(age)
        print('insrted into database')
    else:
        raise TypeError('incorrect data type')

insert_patient_id('chirag',21)

