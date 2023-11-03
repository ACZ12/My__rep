import numpy as np
import pandas as pd
nums= [33,54,76,23,78,56,67]
evens=[]
odds=[]
for num in nums:
    if num%2==0:
        evens.append(num)
    else:
        odds.append(num)
print(evens,odds)
npevens=np.array(evens)
npodds=np.array(odds)
sum=npevens+npodds
print(sum)
