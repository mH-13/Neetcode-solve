from typing import List

numbers=[-5,-3,0,2,4,6,8]
target=5
l, r = 0, len(numbers)-1
res = []

while l<r:
    if numbers[l] + numbers[r] > target:
        r -= 1
    elif numbers[l] + numbers[r] < target:
        l += 1
    else:
        res.extend([l+1, r+1])
        break

print(res)
        
