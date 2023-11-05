def dec(func):
    def wrapper(*args,**kwargs):
        print('started')
        func(*args,**kwargs)
        print('ended')
    return wrapper

from functools import *
@dec
def add(a,b):
    print(a+b)

add(2,4)

def dec2(func):
    def wrapper(*args):
        print("stra")
        func(*args)
        print("end")
    return wrapper

@dec2
def sub(*args):
    print(reduce(lambda x,y:x-y,args))
sub(5,4,3,3)

def dec3(func):
    def wrapper(*args):
        print("STARTED")
        func(*args)
        print("ended")
    return wrapper

@dec3
def fil(*args):
    print(list(filter(lambda x:x>5,args)))
fil(1,4,5,6,7,8)