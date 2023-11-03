from threading import Thread
from time import *
def t1():
    while 1:
        print(ctime())
        sleep(1)

def t2():
    while 1:
        print(ctime())
        sleep(1)

t11=Thread(target=t1)
t22=Thread(target=t2)
t11.start()
t22.start()
        
