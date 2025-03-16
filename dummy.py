from typing import List

nums=[2,20,4,10,3,4,5]
res = 0
lst = set(nums)
print(lst)

for n in nums:
    strek = 0
    curr = n
    while curr in lst:
        strek += 1
        curr +=1

    res = max(res, strek)
