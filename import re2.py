import re

if re.match("^[\w\.\-]+[@][a-z]+[\.][a-z]{2,3}$","adam.cyene2007@gmail.com"):
    print("1")
else:
    print("0")
    
match=re.search("^(?P<fn>\w+) (?P<nn>\w+)$","Adam Czene")
if match:
    print(match.group("fn"))
    print(match.group("nn"))
else:
    print("0")
    
pattern=re.search("[dog][horse]","The quick brown fox jumps over the lazy dog.")
if pattern:
    print("1")
else:
    print("0")

    