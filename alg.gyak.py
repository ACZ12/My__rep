arr=[4,2,1,3,5]

def inssort(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
inssort(arr)
print(arr)

arr2=[3,2,4,1,5]

def inssort2(arr2):
    for i in range(1,len(arr2)):
        j=i
        while arr2[j-1]>arr2[j] and j>0:
            arr2[j-1],arr2[j]=arr2[j],arr2[j-1]
            j-=1
inssort2(arr2)
print(arr2)
                   
arr3=[3,2,4,1,5]
def inssort3(arr3):
    for i in range(1,len(arr3)):
        j=i
        while arr3[j-1]>arr3[j] and j>0:
            arr3[j-1],arr3[j]=arr3[j],arr3[j-1]
            j-=1
inssort3(arr3)
print(arr3)

arr4=[3,2,4,1,5]
def selsort(arr4):
    for i in range(0,len(arr4)-1):
        curmin=i
        for j in range(i+1,len(arr4)):
            if arr4[j]<arr4[curmin]:
                curmin=j
        arr4[i],arr4[curmin]=arr4[curmin],arr4[i]
selsort(arr4)
print(arr4)

arr=[1,4,2,5,3]
def selsort2(arr):
    for i in range(0,len(arr2)-1):
        curmin=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[curmin]:
                curmin=j
        arr[i],arr[curmin]=arr[curmin],arr[i]
selsort2(arr)
print(arr)

arr=[3,1,4,6,65,3,2,1,11,3,55]
def selsort3(arr):
    for i in range(0,len(arr)-1):
        curmin=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[curmin]:
                curmin=j
        arr[i],arr[curmin]=arr[curmin],arr[i]
selsort3(arr)
print(arr)

arr=[4,2,5,67,876,34,2]
def inssort4(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            i-=1
inssort4(arr)
print(arr)
            
import random
arr=[random.randint(0,100) for i in range(10)]
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

arr=[random.randint(0,100) for i in range(10)]
def mergesort2(arr):
    if len(arr)>1:
        left=arr[:len(arr)//2]
        right=arr[len(arr)//2:]
        mergesort2(left)
        mergesort2(right)
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
mergesort2(arr)
print(arr)

arr=[random.randint(0,100) for i in range(100)]
def selsort4(arr):
    for i in range(0,len(arr)-1):
        curmin=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[curmin]:
                curmin=j
        arr[i],arr[curmin]=arr[curmin],arr[i]
selsort4(arr)
print(arr)

arr=[random.randint(0,100) for i in range(10)]
def inssort5(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1

inssort5(arr)
print(arr)

arr=[random.randint(0,100) for i in range(10)]
def mergesort3(arr):
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
mergesort3(arr)
print(arr)

arr=[random.randint(0,100) for i in range(100)]

def mergesort4(arr):
    if len(arr)>1:
        left=arr[:len(arr)//2]
        right=arr[len(arr)//2:]
        mergesort4(left)
        mergesort4(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                j+=1
            else:
                arr[k]=right[j]
                i+=1
            k+=1
        while i<len(left):
            arr[k]=left[i]
            j+=1
            k+=1
        while j<len(right):
            arr[k]=right[i]
            k+=1
            j+=1   
mergesort3(arr)
print(arr)

arr=[random.randint(0,100) for i in range(100)]
def mergesort5(arr):
    if len(arr)>1:
        left=arr[:len(arr)//2]
        right=arr[len(arr)//2:]
        mergesort5(left)
        mergesort5(right)
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
mergesort5(arr)
print(arr)

arr=[random.randint(0,100) for i in range(100)]
def mergesort6(arr):
    if len(arr)>1:
        left=arr[:len(arr)//2]
        right=arr[len(arr)//2:]
        mergesort6(left)
        mergesort6(right)
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
mergesort6(arr)
print(arr)

arr=[random.randint(0,100) for i in range(100)]
def mergesort7(arr):
    if len(arr)>1:
        left=arr[len(arr)//2:]
        right=arr[:len(arr)//2]
        mergesort7(left)
        mergesort7(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]< right[j]:
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
mergesort7(arr)
print(arr)

arr=[random.randint(0,100) for i in range(100)]
def inssort6(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
inssort6(arr)
print(arr)

arr=[random.randint(0,100) for i in range(100)]
def selsort4(arr):
    for i in range(0,len(arr)-1):
        curmin=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[curmin]:
                curmin=j
        arr[i],arr[curmin]=arr[curmin],arr[i]
selsort4(arr)
print(arr)
    
arr=[random.randint(0,100) for i in range(100)]
def selsort5(arr):
    for i in range(0,len(arr)):
        curmin=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[curmin]:
                curmin=j
        arr[i],arr[curmin]=arr[curmin],arr[i]
selsort5(arr)
print(arr)
arr=[random.randint(0,100) for i in range(100)]
def inssort7(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
            
inssort7(arr)
print(arr)

arr=[random.randint(0,100) for i in range(100)]
def mergesort8(arr):
    if len(arr)>1:
        left=arr[:len(arr)//2]
        right=arr[len(arr)//2:]
        mergesort7(left)
        mergesort7(right)
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
mergesort8(arr)
print(arr)

arr=[random.randint(0,100) for i in range(100)]
def mergesort9(arr):
    if len(arr)>1:
        left=arr[:len(arr)//2]
        right=arr[len(arr)//2:]
        mergesort9(left)
        mergesort9(right)
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
mergesort9(arr)
print(arr)

arr=[random.randint(0,100) for i in range(100)]
def selsort5(arr):
    for i in range(0,len(arr)-1):
        curmin=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[curmin]:
                curmin=j
        arr[i],arr[curmin]=arr[curmin],arr[i]
selsort5(arr)
print(arr)

arr=[random.randint(0,100) for i in range(100)]
def inssort8(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
inssort8(arr)
print(arr)

arr=[random.randint(0,100) for i in range(100)]
def selsort6(arr):
    for i in range(0,len(arr)):
        curmin=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[curmin]:
                curmin=j
        arr[i],arr[curmin]=arr[curmin],arr[i]
selsort6(arr)
print(arr)

arr=[random.randint(0,100) for i in range(100)]
def inssort9(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
inssort9(arr)
print(arr)
    
arr=[random.randint(0,100) for i in range(100)]
def selsort7(arr):
    for i in range(0,len(arr)-1):
        curmin=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[curmin]:
                curmin=j
        arr[i],arr[curmin]=arr[curmin],arr[i]
selsort7(arr)
print(arr)

arr=[random.randint(0,100) for i in range(100)]
def inssort10(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1   
inssort10(arr)
print(arr) 

arr=[random.randint(0,100) for i in range(100)]
def mergesort10(arr):
    if len(arr)>1:
        left=arr[:len(arr)//2]
        right=arr[len(arr)//2:]
        mergesort10(left)
        mergesort10(right)
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
mergesort10(arr)
print(arr)

arr=[random.randint(0,100) for i in range(100)]
def selsort8(arr):
    for i in range(0,len(arr)-1):
        curmin=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[curmin]:
                curmin=j
        arr[i],arr[curmin]=arr[curmin],arr[i]

selsort8(arr)
print(arr)

arr=[random.randint(0,100) for i in range(100)]
def inssort11(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
            
inssort11(arr)
print(arr)

arr=[random.randint(0,100) for i in range(100)]
def mergesort11(arr):
    if len(arr)>1:
        left=arr[:len(arr)//2]
        right=arr[len(arr)//2:]
        mergesort11(left)
        mergesort11(right)
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
mergesort11(arr)
print(arr)

arr=[random.randint(0,100) for i in range(100)]
def quicksort(arr,left,right):
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
        arr[i],arr[j]=arr[j],arr[i]
    return i

quicksort(arr,0,len(arr)-1)

arr=[random.randint(0,100) for i in range(100)]
def mins(arr):
    mmin=arr[0]
    for i in range(len(arr)):
        if arr[i] < mmin:
            mmin=arr[i]
    print(mmin)

mins(arr)

arr=[random.randint(0,100) for i in range(100)]
def maxs(arr):
    mmax=arr[0]
    for i in range(len(arr)):
        if mmax<arr[i]:
            mmax=arr[i]
    print(mmax)
        
maxs(arr)

def mergesort12(arr):
    if len(arr)>1:
        left=arr[:len(arr)//2]
        right=arr[len(arr)//2:]
        i=0
        j=0
        k=0
        mergesort12(left)
        mergesort12(right)
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
mergesort12(arr)
print(arr)    
arr=[random.randint(0,100) for i in range(100)]
def mergesort13(arr):
    if len(arr)>1:
        left=arr[:len(arr)//2]
        right=arr[len(arr)//2:]
        i=0
        j=0
        k=0
        mergesort13(left)
        mergesort13(right)
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

                
mergesort13(arr)
print(arr)
        
def bubsort(arr):
    indexing_length=len(arr)-1 
    sorted = False 

    while not sorted:  
        sorted=True  

        for i in range(0,indexing_length): 
            if arr[i]:
                sorted=False 
                arr[i],arr[i+1]=arr[i+1],arr[i] 
    return list_a 

arr=[random.randint(0,100) for i in range(100)]
bubsort(arr)
print(arr)

def inssort(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j]<arr[j-1]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
arr=[random.randint(0,100) for i in range(100)]
inssort(arr)
print(arr)

def inssort(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
arr=[random.randint(0,100) for i in range(100)]
inssort(arr)
print(arr)

def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i=0
        r=[]
        while i<len(strs[0]):
            l1=strs[0][i] 
            l2=strs[1][i] 
            l3=strs[2][i] 
            if l1==l2 and l1==l3:
                r.append(l1)
                i+=1
        return "".join(r)
    
longestCommonPrefix(["abc","abcd","abcde"])

arr=[random.randint(0,50) for i in range(50)]
def bubsort6(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
bubsort6(arr)
print(arr)
                