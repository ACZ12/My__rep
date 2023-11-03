from collections import *


a=deque("ogre")
a.extend("gg")
a.pop()
a.popleft()
print(a)
print (Counter("aeiou"))

m=str.maketrans("aeio","1234","u")
mondat="eaiou"
print(mondat.translate(m))

b=("a","b","c")
a=iter(b)
for i in b:
    print(next(a))


def check(func):
    def inside(x,y):
        if y==0:
            print("egyenlo")
            return
        func(x,y)
    return inside

@check
def add(x,y):
    return x+y

print(add(4,2))