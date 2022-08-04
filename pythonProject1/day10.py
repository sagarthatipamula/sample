"""
#Oops
#object oriented programming system
#class - class is blueprint
#object/instance- Object created using class blueprint


#algorithm
#A class is a collection of attributes(variables) and methods
#syntax
#class<classmate>:
#     <attributes>
#    <methods>
class Employee:
    employee_name= "Raju"
    def fetch_employee_details(self):
        return {"name":"ramesh", "age":25}
ramesh_obj = Employee()

print(ramesh_obj.employee_name)
print(ramesh_obj.fetch_employee_details())


class student:
    student_name= "jaichandra"
    student_grade= "A+"
    student_age= "24"
    student_div= "A"

    def student_details(self):
        return {"Name":"Jaichandra", "Age":24, "grade":"A", "Div":"A"}
student_obj= student()
print(student_obj.student_div)
print(student_obj.student_grade)
print(student_obj.student_name)
print(student_obj.student_age)
print(student_obj.student_details())




class humanbeing:
    colour= "white"
    height= "5.4"
    age=     "26"
    fitness= "good"

    def description_human(self):
        return {"colour":"white", "age":34, "height":5 }

humanbody_details_object= humanbeing()
print(humanbody_details_object.age)
print(humanbody_details_object.height)
print(humanbody_details_object.colour)
print(humanbody_details_object.fitness)
print(humanbody_details_object.description_human())










class cardetails:
    name="BMW"
    model_no= "720D"
    colour= "Matt Black"
    Top_speed= 285
    sunroof= "yes"

    def detailing_of_BMW_car(self):
        return {"name":"BMW", "model_no": "720D", "colour":"Matt Black"}
car_details_obj= cardetails()
print(car_details_obj.colour)
print(car_details_obj.name)
print(car_details_obj.Top_speed)
print(car_details_obj.model_no)
print(car_details_obj.detailing_of_BMW_car())



class numbers:

    list1=[1,2,3,4]
    list2=[5,6,7,8]
    def calc(self):
        list1=[9,10,11,12]

        list2=[13,14,15,16]

        return list1+list2

list_object=numbers()
print(list_object.list1)
print(list_object.list2)
print(list_object.calc())
"""

class cricket:
    a=["batting"]
    b=["ball"]
    c=["stumps"]
    d=["gloves"]

    def batsmen(self):
        global a
        a = ["bat"]
        b = ["ball"]
        c = ["stumps"]
        d = ["gloves"]
        return a+b+c+d

cricket_things=cricket()
print(cricket_things.a)
print(cricket_things.b)
print(cricket_things.c)
print(cricket_things.d)
print(cricket_things.batsmen())


import time
list=[1,2,3,4]
for item in list:
    print(item)
    time.sleep(2)










