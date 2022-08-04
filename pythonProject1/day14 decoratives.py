"""import time


def fun_exec_time_cal(sagar):
    print("{} being executed".format(sagar.__name__))

    def Wrapper():
        start_time = time.time()
        sagar()
        end_time = time.time()
        print("{} took seconds".format(end_time - start_time))

    return Wrapper


@fun_exec_time_cal
def fun1():
    time.sleep(2)
    a = 10
    time.sleep(2)
    print("a is {}".format(a))


fun1()
#
import time

start_time = time.time()
a = 20
end_time = time.time()
print("program took {} secs to execute for a = 10".format(end_time - start_time))
b = 40
end_time = time.time()
print("program took {} secs to execute for b=40".format(end_time - start_time))
while True:
    if a < b:
        print("a is {}".format(a))
        break
    end_time = time.time()
    print("program took {} secs to execute for condition".format(end_time - start_time))

import time


def fun(pavan):
    print("{} being executed".format(pavan.__name__))

    def wrapper():
        start_time = time.time()
        pavan()
        end_time = time.time()
        print("program took {} secs ".format(end_time - start_time))

    return wrapper


@fun
def fun2():
    time.sleep(2)
    a = 20
    time.sleep(2)
    print("a is {}".format(a))


fun2()


def function(name):
    def func1():
        name()
        a = 10
        b = 20
        print(a + b)

    return func1


@function
def func2():
    a = 50
    b = 20
    print(a + b)


func2()


def substraction(abc):
    def sub():
        abc()
        a = 90
        b = 45
        print(a - b)

    return sub


@substraction
def xyz():
    print("wcwf")


xyz()

import time


def ash(wsh):
    print("{} being executed".format(wsh.__name__))

    def hh():
        start_time = time.time()
        wsh()
        end_time = time.time()
        print("program took {} secs to execute".format(end_time - start_time))

    return hh


@ash
def wh():
    time.sleep(2)
    a = 50
    time.sleep(2)
    print("a is {}".format(a))


wh()

import time


def woodstork(hills):
    print("{} is being executed".format(hills.__name__))

    def boho():
        start_name = time.time()
        hills()
        end_name = time.time()
        print("program took {} secs to execute".format(end_name - start_name))

    return boho


@woodstork
def westwoods():
    time.sleep(1)
    a = 10
    b = 20
    time.sleep(1)
    print("addition of a and b is {} ".format(a + b))


westwoods()


def car_company(Details):
    print("{} is being executed ".format(Details.__name__))

    def bike_details():
        a = 10
        b = 20
        Details()
        print("addition of a and b is {}".format(a + b))

    return bike_details


@car_company
def Auto_parts():
    x = 30
    y = 40
    print("substraction of x and y is {}".format(x - y))


Auto_parts()

import time

start_time = time.time()


def abc(ddd):
    def xyz():
        a = 10
        b = 20
        ddd()
        print(a + b)

    return xyz


@abc
def pqr():
    for item in range(6):
        print(item)
        time.sleep(2)


pqr()
"""

def student_details(detailing):
    def add():
        a = 10
        b = 20
        detailing()
        print(a+b)

    return add


@student_details
def subs():
    p = 20
    q = 30
    print(p + q)


subs()
