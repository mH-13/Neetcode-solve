

nums = [1,2,3,4]
n = len(nums) 
res = []
prefix = [1] * n
postfix =[1] * n
pref = 1
postf = 1

for i in range(0, len(nums)):
    if (i ==0):
        prefix.append(nums[i])
    else:                
        pref = nums[i] * prefix[i-1]
        prefix.append(pref)
print(prefix)

#postfix array creation

for i in range(n-1,-1, -1):
    print(i)
    if (i == n-1):
        postfix[i] = nums[i]
    else:
        postf = nums[i] * postfix[i+1]
        postfix[i] = postf
        
print(postfix)
