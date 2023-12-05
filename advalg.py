def twopointer(arr,target):
    l=0
    r=len(arr)-1
    while l<r:
        sum=arr[l]+arr[r]
        if sum==target:
            print(l,r)
            break
        elif sum<target:
            l+=1
        else:
            r-=1

arr=[1,2,3,4,5,6,7,8,9,0]
target=3
twopointer(arr,target)

def twopointer2(arr,target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            sum=arr[i]+arr[j]
            if sum==target:
                print(i,j)
                j+=1
                continue
        
twopointer2([1,3,4,6,7,3,9,0],10)
