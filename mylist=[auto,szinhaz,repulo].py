def fib(s):
    a,b=1,1
    result=[]
    for i in range(s):
        result.append(a)
        c=b
        b+=a
        a=c
    
    print(result)
fib(30)