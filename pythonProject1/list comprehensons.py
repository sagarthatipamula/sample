"""my_list = range(101)
odd_list = []
for item in my_list:
    if item %2!=0:
        odd_list.append(item)
        print(item)

#with list comprehensons
Odd_list = [item for item in range(100) if item %2!=0 ]
print(odd_list )

#without list comprehensons
import time
start_time=time.time()
mylist = range (100)
oddlist = []
for item in mylist:
    print("value is {}".format(item))
    if item %2!=0:
        oddlist.append(item)
        print("odd list is {}".format(oddlist))
    else:
        print("Is {} even number? {}".format(item, item %2!=0))
        print()
        end_time = time.time()
        print("To create a oddlist it took {} secs".format(end_time-start_time))

import time
start_time = time.time()
odd_name = [item for item in range(100) if item %5==0]
print(odd_name)
end_time=time.time()
print("to create a func it took {} seconds ".format(end_time-start_time))

Int_list = [item for item in [1,2,"India", [4,5]]if type(item)==int]
print(Int_list)

str_list = [item for item in [1,2,"India", [4,5]]if type(item)==str]
print(str_list)

my_list = [item for item in [1,2,"India", [4,5]]if type(item)==list]
print(my_list)




#Dict comprehensons
my_list = [1,2,3,4,5,6]
#output to come in {1:True, 2:False, 3:True, 4:False, 5:True, 6:False}
my_dict = {item:True if item %5!=0 else False for item in my_list}
print(my_dict)

sagar= {1:{2:{3:100}}}
print("sagar[1] is",sagar[1])
print("sagar[1] is",sagar[1][2])
print("sagar[3] is ", sagar[1][2][3])


mlist = range(10)
my_D2 = {item:True if item %3==0 else False for item in mlist}
print(my_D2)


mlist = range(10)
my_D2 = {item:True if item %3!=0 else False for item in mlist}
print(my_D2)
print()

list = [(1,2,3), {10:222}, {"sagar"}, 0.2]
list2=[item for item in list if type(item)==float]
print(list2)

list = [(1,2,3), {10:222}, {"sagar"}, 0.2]
list2=[item for item in list if type(item)==set]
print(list2)

list = [(1,2,3), {10:222}, {"sagar"}, 0.2]
list2=[item for item in list if type(item)==tuple]
print(list2)

list = [(1,2,3), {10:222}, {"sagar"}, 0.2]
list2=[item for item in list if type(item)==dict]
print(list2)

list = [(1,2,3), {10:222}, {"sagar"}, 0.2]
list2=[item for item in list[2]]
print(list2)

list = [(1,2,3), {10:222}, {"sagar"}, 0.2]
list2=[item for item in list[0]]
print(list2)





numbers = []
for i in range(1,100):
   numbers.append(i)
   print(i)

list = [1,2,3,4,6,7]
numbers = [item for item in list if 2 not in list ]
print(False)

list = range(50)
list3 = [numbers for numbers in list if numbers %5==0]
print(list3)

list = range(30)
web=[ss for ss in list if ss %2==0 if ss %5==0]
print(web)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hiii'for item in fruits ]
print(newlist)


fruits = [1,2,4,5,7,8]

newlist = [x if x ==1 else "sgr" for x in fruits]

print(newlist)





mlist = [1,2,3,4,5,6,7,8,9]
my_D2 = {item:True if item %3==0 else False for item in mlist}
print(my_D2)

newlist = [x for x in range(10) if x > 5]
print(newlist)


list= range(30)
list2=[x for x in list if x %3==0]
print(list2)

numbers = []
for i in range(1,100):
   numbers.append(i)
   print(i)


ee={1:{2:{3:{4:{5:{6:{7:8}}}}}}}
print("mydict is ",ee[1])
print("mydict is ",ee[1][2])
print("mydict is ",ee[1][2][3])


ttt = {"a":{"b":{"c":{"d":{"e":{"f":"g"}}}}}}
print("mydict2 is ",ttt["a"])
print("mydict2 is ",ttt["a"]["b"])
print("mydict2 is ",ttt["a"]["b"]["c"])
print("mydict2 is ",ttt["a"]["b"]["c"]["d"])
print("mydict2 is ",ttt["a"]["b"]["c"]["d"]["e"])
print("mydict2 is ",ttt["a"]["b"]["c"]["d"]["e"][f])

mylist = ["a","e","i","o","u"]
q4_answer = "sagar".join([item for item in mylist if item not in ["a","e","i","o","u"]])
print(mylist)

"""
# list = [1,2,3,56,442,2323]
# # list2 = [for item in list if item i]
# cars = ["Aston", "Audi", "McLaren"]
# i = len(cars[0])
# print(i)
#
# cars = ["Aston" , "Audi", "McLaren "]
# a= enumerate(cars)
# print(a)
#
# print("\nTuple Iteration")
# t = ("geeks", "for", "geeks")
# for i in t:
#     print(i)
#
# a=[1,2,3,4]
# for i in a:
#    print(i)

# # Empty list
# List = []
#
# # Traditional approach of iterating
# for aa in 'Geeks 4 Geeks!':
#     List.append(aa)
#
# # Display list
# print(List)
#
#
#
# list = []
#
# for abc in 'sagar':
#     list.append(abc)
#     print(list)


# def add(input1,input2):
#     print("Type of input1 is {}".format(type(input1)))
#     print("type of input2 is {}".format(type(input2)))
#     if type(input1) == int and type(input2) == int:
#         print("The addition of input1 and input2 is {}".format(input1+input2))
#
#     else:
#         print("it doesnt matches the condition")
#
# add(10,25)

# mlist = range(10)
# my_D2 = {item:True if item %3!=0 else False for item in mlist}
# print(my_D2)


MY = range(50)
myyy = {item: [1,2,3] if item % 5 != 0 else {1: {2:3}} for item in MY}
print((myyy))

