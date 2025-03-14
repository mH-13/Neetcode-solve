

nums=[4,3,2,1,2]


print("nums ", nums)
n = len(nums)
res = [1] * n
prefix = [1] * n
postfix =[1] * n
pref = 1
postf = 1


for i in range(0, n):
    if (i ==0): 
        prefix[i] = nums[i]
    else:
        prefix[i] = nums[i] * prefix[i-1]

print("prefix ", prefix)

for i in range(n-1, -1, -1):
    if i == n-1:
        postfix[i] = nums[i]
    else:
        postfix[i] = nums[i] * postfix[i+1]

print("postfix ", postfix)



for i in range(0, n):
    if i == 0: 
        res[i] = postfix[i+1]
    elif i == n-1: 
        res[i] = prefix [i-1]
    else:
        res[i] = prefix[i-1] * postfix[i+1]


print("-------------------")        
print("res ", res)
