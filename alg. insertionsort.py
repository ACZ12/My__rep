arr=[2,3,5,4,3]
def ssort(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
        
ssort(arr)
print(arr)
    
