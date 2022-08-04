# functions
# function returning values
"""

def add(x,y):
    return(x+y)
print(add(10,20))


#write a sample function to return
#your_name+sharma as lastname



def add_name(name):
    return name+ "add"
print(add_name("sagar"))



def fullname( name, middle):
    return name+ middle+ "adda"
print(fullname("sagar","manohar"))




def addname(firstname):
    return(firstname+"sharma")

    print("india")
    print("mum")

print(addname("sagar"))







import time
list= range (20)
for item in list:
    if item %2==0:
        print (item)
       time.sleep(.5)




def add(list1,list2):
    print("type of list1 is", type(list1))
    print("type of list2 is", type(list2))
    if type(list1)==int and type(list2)==int:
        print("addition is", list1+list2)

    else:
        if type(list1)!=int:
            print("list1 is invalid int pls allow only float num")
        if type(list2)!=int:
            print("list2 is invalid int pls allow only float num")

add(10,20.4)



#*arguments,
#**keyword arguments



#we use this when the user dont know the no of inputs will take

"""


def add(*input):
    print(input)
    return sum(input)


print(add())
print()
print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))


def sub(*list):
    print(list)
    return len(list)


print(sub())
print()
print(sub(1, 2, 3, 4, 5, 6, 6, 7, 8, 9))

def add(firstname):
    return firstname + "sharma"




print(add("sagar"))







































































