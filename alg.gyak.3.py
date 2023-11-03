import random
def mergesort(arr):
    if len(arr)>1:
        left=arr[:len(arr)//2]
        right=arr[len(arr)//2:]
        mergesort(left)
        mergesort(right)
        j=0
        i=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1

arr=[random.randint(0,50) for i in range(50)]
mergesort(arr)
print(arr)

def quicksort(arr,left,right):
    if left<right:
        partpos=partition(arr,left,right)
        quicksort(arr,left,partpos-1)
        quicksort(arr,partpos+1,right)
def partition(arr,left,right):
    i=left
    j=right-1
    pivot=arr[right]
    while i<j:
        while i<right and arr[i]<pivot:
            i+=1
        while j>left and arr[j]>=pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    if arr[i]>pivot:
        arr[i],arr[right]=arr[right],arr[i]
    return i
arr=[random.randint(0,50) for i in range(50)]
quicksort(arr,0,len(arr)-1)
print(arr)

def bisearch(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            print(mid)
            break
        elif arr[mid]<target:
            left=mid+1
        else: 
            right=mid-1
arr=[1,2,3,4,5,6]
bisearch(arr,2)

def bisearch(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            print(mid)
            break
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
arr=[1,2,3,4,5,6]
bisearch(arr,2)

def bisearch(arr,target):
    left=0
    right=len(arr)-1 
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            print(mid)
            break
        elif arr[mid]<target:
            left=mid+1
        else:right=mid-1
arr=[1,2,3,4,5,6]
bisearch(arr,2)

def bisearch(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            print(mid)
            break
        elif arr[mid]>target:
            right=mid-1
        else:
            left=mid+1
arr=[1,2,3,4,5,6,6,7,8,9]
bisearch(arr,4)

def selsort(arr):
    for i in range(len(arr)-1):
        curmin=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[curmin]:
                curmin=j
        arr[i],arr[curmin]=arr[curmin],arr[i]
arr=[random.randint(0,50) for i in range(50)]
selsort(arr)
print(arr)

def bubsort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j+1]<arr[j]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[random.randint(0,50) for i in range(50)]
bubsort(arr)
print(arr)        

def inssort(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j]<arr[j-1] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
arr=[random.randint(0,50) for i in range(50)]
inssort(arr)
print(arr)     

def mergesort(arr):
    if len(arr)>1:
        left=arr[:len(arr)//2]
        right=arr[len(arr)//2:]
        mergesort(left)
        mergesort(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
arr=[random.randint(0,50) for i in range(50)]
mergesort(arr)
print(arr) 
    
    
def quicksort(arr,left,right):
    partpos=partition(arr,left,right)
    quicksort(arr,left,partpos-1)
    quicksort(arr,partpos+1,right)
    
def partition(arr,left,right):
    i=left
    j=right-1
    pivot=arr[right]
    while i<j:
        while i<right and arr[i]<pivot:
            i+=1
        while j>left and arr[j]>=pivot:
            j-=1
        if i>j:
            arr[i],arr[j]=arr[j],arr[i]
    if arr[i]>pivot:
        arr[i],arr[right]=arr[right],arr[i]
    return i
arr=[random.randint(0,50) for i in range(50)]
quicksort(arr,0,len(arr)-1)
print(arr) 

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