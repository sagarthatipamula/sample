#json(java script object notation)
#json is widely used for data transfer in the web
#client ---> server
#server ---> client
"""
json.loads() -- JSON String to Python native datatype  (DeSerialization)
json.dumps() -- Python Native datatype to JSON String (Serialization)


import json
myJsonList = "[1,2,3,4,5]"
print(myJsonList)
print("MyJsonList type is{}".format(type(myJsonList)))
print("oth index of myJsonList is {}".format(myJsonList[0]))
mylist = json.loads(myJsonList)
print("myList type is {}".format(type(mylist)))
print("0th index of myList is {}".format(mylist[0]))
print(mylist)
mylist2 = json.dumps(mylist)
print("type of mylist2 is {}".format(type(mylist2)))
print("3rd index of my myList {}".format(mylist2[4]))
print()
myJsonDict = '{"name":"Raghu", "age":30}'
print("type of myJsonDict is {}".format(type(myJsonDict)))
print(myJsonDict)
myDict = json.loads(myJsonDict)
print("type of myDict is {}".format(type(myDict)))
print("value of myDict[name] is {}".format(myDict["name"]))
print(myDict)
myDict2 = json.dumps(myDict)
print("type of myDict2 is {}".format(type(myDict2)))
print(myDict2)
print("3rd index value of myDict2 is {}".format(myDict2[9]))
print()



# import json
# myJson_list = '[{"a":1,"b":2,"c":3},{"a":5, "b":10}]'
# print("myJson_list list is {}".format(myJson_list))
# print("type of myJson_list is {}".format(type(myJson_list)))
# mylist3 = json.loads(myJson_list)
# print("type of my mylist3 is {}".format(type(mylist3)))
# print("2nd index value mylist3 is {}".format(mylist3[1]))
# print(mylist3)
# mydictlist = json.dumps(myJson_list)
# print("type of mydictlist is {}".format(type(mydictlist)))
# print(mydictlist)
# mydict3 = json.loads(mydictlist)
# print(mydict3)
# print(type(mydict3))
# print(mydict3)
# mydict4 = json.loads(mydict3)
# print("type of mydict4 is {}".format(type(mydict4)))
# mydict4[0].update({"d":50})
# print(mydict4)


import json
my_list_dict = [{"a":500, "b":100}, {"c":150, "d":55}, {"e":22}]
print("type of my_list_dict is {}".format(type(my_list_dict)))
dict1 = json.dumps(my_list_dict)
print("type of dict1 is {}".format(type(dict1)))
print(dict1)
dict2 = json.loads(dict1)
print("type of dict2 is {}".format(type(dict2)))
print(dict2)
dict2[2].update({"g":44})
print(dict2)

"""
# import json
#
# myJsonstring = '["India"]'
# print("type of myJsonstring is {}".format(type(myJsonstring)))
# d4 = json.loads(myJsonstring)
# print(d4)
# print(type(d4))
# d5 = json.dumps(d4)
# print(d5)
# print(type(d5))
#
#
# import json
#
# my_list_dict="[{'a':{'c':{'b':33}}}]"
# print("type of my_list_dict is {}".format(type(my_list_dict)))
# D1=json.dumps(my_list_dict)
# print(D1)
# print("type pf D1 is {}".format(type(D1)))
# d2=json.loads(D1)
# print(d2)
# print(type(d2))
# d3=json.dumps(d2)
# print(d3)
# d4 = json.loads(d3)
# print(d4)
# print("{}".format(type(d4)))

import json
list = '[{"abc":111},{"def":222}]'
print("type of list is {}".format(type(list)))
list2 = json.loads(list)
print("type of list2 is {}".format(list2))
list2[1].update({"efg":333})
print(list2)

import json
list = '[{"abc":111},{"def":222}]'
print("type of list is {}".format(type(list)))
list2 = json.loads(list)
print("type of list2 is {}".format(list2))
list2.extend({"efg":333})
print(list2)



list = '[1,2,4,5]'
liat_2 = '[4,5,]'

































