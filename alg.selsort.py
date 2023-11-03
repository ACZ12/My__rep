arr=[5,3,2,1,4]

def selsort(arr):
    for i in range(0,len(arr)):
        curmin=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[curmin]:
                curmin=j
        arr[i],arr[curmin]=arr[curmin],arr[i]
            
        
selsort(arr)
print(arr)

arr2=[3,4,2,1,5]
def inssort(arr2):
    for i in range(1,len(arr2)):
        j=i
        while arr2[j-1]>arr2[j] and j>0:
            arr2[j-1],arr2[j]=arr2[j],arr2[j-1]
            j-=1
    

inssort(arr2)
print(arr2)
            