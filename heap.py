import random
def maxheap(arr,n,parentidx):
    largest=parentidx
    left=2*parentidx+1
    right=2*parentidx+2
    
    if left<n and arr[left]>arr[largest]:
        largest=left
    if right<n and arr[right]>arr[largest]:
        largest=right
    if largest!=parentidx:
        arr[largest],arr[parentidx]=arr[parentidx],arr[largest]
        maxheap(arr,n,largest)
        
def heapsort(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        maxheap(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        maxheap(arr,i,0)

arr=[random.randint(0,50) for i in range(50)]
heapsort(arr)
print(arr)