import logic
import os
logic.f(30,40)
print (os.getcwd())
os.chdir("C:\My__rep")
print (os.getcwd())
#if os.getcwd()!="C:\My__rep\\ttt":
    #os.rmdir("C:\My__rep\\ttt")
#else:
    #os.chdir("C:\My__rep")
    #os.rmdir("C:\My__rep\\ttt")
current=os.getcwd()
pics="var.py"
combined=os.path.join(current,pics)
os.rename("var.py","varr.py")
print(combined)
print (os.getlogin())