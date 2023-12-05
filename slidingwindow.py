def slwd(arr,sub):
    for i in range(len(arr)-len(sub)+1):
        if arr[i:i+len(sub)]==sub:
            return True
    return False 
print(slwd([1,2,3,4,5,6,7,8],[5,6]))