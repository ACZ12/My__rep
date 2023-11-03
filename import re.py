import re

pattern="[A-Za-z0-9]+@[a-zA-Z0-9]+\.(net|com|sk)"
pas=input()
if re.search(pattern,pas):
    print ("yes")
else:
    print("no")