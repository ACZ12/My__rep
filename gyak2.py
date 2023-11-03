from threading import Thread
from time import *

def t():
    while 1:
        print(ctime())
        sleep(1)
        
tt=Thread(target=t)
#tt.start()

a=["a","b","c"]
for i,j in enumerate(a):
    if j=="c":
        print(i,".",j,end=", ")
        
        
a=["a","b","c"]
b=["a","b","c"]
print([(i,j) for i in a for j in b])

from collections import *

a=["a","b","c"]
print(Counter(a))
b=deque("hello")
b.extendleft("ogre")
b.popleft()
print(b)

for i in a:
    print(a.index(i))
