import random
arr=[random.randint(0,50) for i in range(50)]
def bubsort6(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
bubsort6(arr)
#print(arr)

arr=[random.randint(0,50) for i in range(50)]
def quicksort(arr,left,right):
    if left<right:
        part_pos=partition(arr,left,right)
        quicksort(arr,left,part_pos-1)
        quicksort(arr,part_pos+1,left)
        
def partition(arr,left,right):
    i=right
    j=left
    pivot=arr[right]
    while i<j:
        while i<right and arr[i]<pivot:
            i+=1
        while j<left and arr[j]>=pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    if arr[i]>pivot:
        arr[i],arr[right]=arr[right],arr[i]
    return i

#quicksort(arr,0,len(arr)-1)

arr=[random.randint(0,50) for i in range(50)]
def quicksort(arr,left,right):
    if left<right:
        part_pos=partition(arr,left,right)
        quicksort(arr,left,part_pos-1)
        quicksort(arr,part_pos+1,left)
        
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
quicksort(arr,0,len(arr)-1)
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

arr=[random.randint(0,50) for i in range(50)]
def bubsort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
bubsort(arr)
print(arr)
arr=[random.randint(0,50) for i in range(50)]
def selsort(arr):
    for i in range(0,len(arr)-1):
        curmin=i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[curmin]:
                curmin=j
        arr[i],arr[curmin]=arr[curmin],arr[i]
selsort(arr)
print(arr)
arr=[random.randint(0,50) for i in range(50)]
def inssort(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j]<arr[j-1] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
inssort(arr)
print(arr)
arr=[random.randint(0,50) for i in range(50)]
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
mergesort(arr)
print(arr)
arr=[random.randint(0,50) for i in range(50)]
def quicksort(arr,left,right):
    if left<right:
        partpos=partition(arr,left,right)
        quicksort(arr,0,partpos-1)
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
quicksort(arr,0,len(arr)-1)
print(arr)

def binsearch(arr,target):
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

arr=[1,2,3,4,5,6,7,8,9,10]
binsearch(arr,10)
print()

def bisearch(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            print(mid)
            break
        elif target<arr[mid]:
            right=mid-1
        else:
            left=mid+1
arr=[2,3,4,5,6,7]
bisearch(arr,4)

def selsort(arr):
    for i in range(0,len(arr)-1):
        curmin=i
        for j in range(i+1,len(arr)):
            if arr[curmin]>arr[j]:
                curmin=j
        arr[i],arr[curmin]=arr[curmin],arr[i]
arr=[random.randint(0,50) for i in range(50)]
selsort(arr)
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

def bubsort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[random.randint(0,50) for i in range(50)]
inssort(arr)
print(arr)

