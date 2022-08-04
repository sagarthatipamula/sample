# #Oops
# """
# it is object oriented programming system
# CLASS- class is a blueprint
# definition- it is a collection of attributes(Variables) and methods(functions) .
# SYNTAX is <class_name>
#           <attirbutes>
#           <methods>
# """
#
# class Employee:
#     Employee_name="Ramesh"
#     def Employee_details(self):
#         return {"name":"Raju", "Age":55}
# emp=Employee()
# print(emp.Employee_name)
# print(emp.Employee_details())
#
# class owner:
#     owner_name= "Suresh"
#
#     def owner_details(self):
#         print("owner age is 55")
# own=owner()
# print(own.owner_name)
# print(own.owner_name)
# print(own.owner_details())
#
# class parents:
#     parent_name= "Manohar"
#     parent_age= 33
#     parent_location="mumbai"
#     def parents_native(self):
#         print("parents native is sircilla")
# par=parents()
# print(par.parent_name)
# print(par.parents_native())
# print(par.parent_location)
# print(par.parent_age)
#
# #inheritance- Coping features(attributes and methods) from one class to other class is called inheritance
#
# #Types of inheritance
# # 1- single inheritance- single child is coping from single parent
# # 2- multiple inheritance- one child class is coping features from multiple parent class
# # 3- multilevel inheritance- child1 is coping features from parent and child2 is coping from child1
# # 4- heirarchical inheritance- many child is coping features from single parent class
# # 5- hybrid inheritance- combination of 2 or more features of above types called hybrid
#
# #single inheritance
# class parent:
#     parent_name= "Manohar"
# class child(parent):
#     print("child name is sushant")
# obj= child()
# print(obj.parent_name)
#
# #multiple inheritance
#
# class company:
#     company_name= "TCS"
# class Director:
#     Director_name= "Raghunath"
# class Manager:
#     Manager_name= "Hemanth"
# class engineer(Manager,Director,company):
#     pass
# eng=engineer()
# print(eng.company_name)
# print(eng.Manager_name)
# print(eng.Director_name)
#
# #multilevel
# class A:
#     name="sagar"
# class B(A):
#     last_name= "Thatipamula"
# class C(B):
#     pass
# class D(C):
#     pass
# class E(D):
#     pass
# F=E()
# print(F.name)
# print(F.last_name)
#
# #heirarchical
# class A:
#     first_name= "sagar"
# class B(A):
#     pass
# class C(A):
#     pass
# class D(A):
#     pass
# abc = D()
# print(abc.first_name)
#
# #hybrid
# class grandpa:
#     graandpa_age= 77
# class grandma:
#     grandmas_age=70
# class parents(grandpa,grandma):
#     pass
# class child1(parents):
#     pass
# class child2(parents):
#     pass
# class son1(child1,child2):
#     pass
# class son2(son1):
#     pass
# class son3(son1):
#     pass
# class son4(son1):
#     pass
# class son5(son1):
#     pass
# son=son5()
# print(son.graandpa_age)
# print(son.grandmas_age)


# constructor
# class my_details:
#     def __init__(self, my_name, my_age, my_native):
#         self.my_name=my_name
#         self.my_age=my_age
#         self.my_native=my_native
#     def employee_details(self):
#         print("employee name is {}".format(self.my_name))
#     def employee_age(self):
#         print("employee age is {}".format(self.my_age))
#     def employee_native(self):
#         print("employee native is {}".format(self.my_native))
# emp = my_details ("sagar",26,"karimnagar")
# emp.employee_details()
# emp.employee_age()
# emp.employee_native()
#
#
#
#
#
#
#
# class abc:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def aaa(self):
#         print("a is {}".format(self.a))
#     def bbb(self):
#         print("b is {}".format(self.b))
#     def ccc(self):
#         print("c is {}".format(self.c))
# eee = abc(10,20,30)
# eee.aaa()
# eee.bbb()
# eee.ccc()
#
#
# class ddd:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#
#     def eee(self):
#         print('name is {}'.format(self.name))
#     def rrr(self):
#         print('age is {}'.format(self.age))
#     def ggg(self):
#         print('gender is {}'.format(self.gender))
#
#
# rrr_obj = ddd('sagar', 25, 'male')
#
# rrr_obj.ggg()
# rrr_obj.rrr()
# rrr_obj.eee()
#
#
# mystr = "india"
# mydict = {}
# for item in mystr:
#     mydict[item] = mystr.count(item)
#     print(mydict)

#
# mylist = [1, 2, 3, 4, 2]
# mylist2 = []
# for item in mylist:
#     if item not in mylist2:
#         mylist2.append(item)
# print(mylist2)
#
# mylist = [1, 2, 3, 4, 5, 7, 9, 15]
# count = 0
# for item in mylist:
#     if item %2==0:
#         count += 1
#         print("count is", count)

# a = [1,3,4,5,6,7]
# b = [3,4,10,11,14]
#
# c = set(a)
# d = set(b)
# print("common item in c and d is ", c & d)
#
#
# print("not common item of c", c-d )
#
# print("not common item of d", d-c)
#
# print("all not common items of c&d", c-d/d-c)

#
# mystr = "India123Hello"
# count = 0
#
#
# def alpha():
#     pass
#
#
# for item in mystr:
#     if item is alpha():
#         count += 1
# print(count)


# myList = [1, 2, 3, "India", 5, 6, 7]
#
#
# def add_fun(input):
#     print(sum([item for item in input if type(item) == int]))
#
#
# add_fun(myList)

#
# def sample_fun(*input_data):
#     Flag = True
#     if input_data:
#         for item in input_data:
#             if type(item)==int:
#                 pass
#             else:
#                 Flag = False
#             return Flag
#         else:
#             return "no arguments pass by the end_user"
#

def sample_fun(*input_data):
    flag = True
    boolean_list = [False for item in input_data if type(item) != 0]
    if False in boolean_list:
        return False
    else:
        True


print(sample_fun(1, 2, "india", "usa"))
