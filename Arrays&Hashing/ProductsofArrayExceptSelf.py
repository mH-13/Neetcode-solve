# Products of Array Except Self
# LeetCode 238 
# Link: https://leetcode.com/problems/product-of-array-except-self/ 


from typing import List


# Brute Force Approach 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []

        for i in range(0, len(nums)):
            # print("i ", i)
            prdct = 1
            
            for j in range(0, len(nums)):
                # print("j: ",j)
                if i != j:
                    prdct *= nums[j]
            res.append(prdct)

        return res

# This approach has a time complexity of O(N^2) where N is the length of the input list nums. The outer loop iterates through each element in the list, and the inner loop calculates the product of all elements except the current element. This results in a quadratic time complexity. 


# Optimized Approach

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = [1] * n
        prefix = [1] * n
        postfix =[1] * n

        for i in range(0, n):
            if (i ==0): 
                prefix[i] = nums[i]
            else:
                prefix[i] = nums[i] * prefix[i-1]

        for i in range(n-1, -1, -1):
            if i == n-1:
                postfix[i] = nums[i]
            else:
                postfix[i] = nums[i] * postfix[i+1]

        for i in range(0, n):
            if i == 0: 
                res[i] = postfix[i+1]
            elif i == n-1: 
                res[i] = prefix[i-1]
            else:
                res[i] = prefix[i-1] * postfix[i+1]
        return res


# This approach has a time complexity of O(N) and a space complexity of O(N) where N is the length of the input list nums. The algorithm calculates the prefix product and postfix product arrays to efficiently compute the product of all elements except the current element. The resulting array contains the desired products for each element in the input list. 



#more optimized 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = [1] * n #
        
        prefix = 1
        for i in range(0, n):
            res[i] = prefix
            prefix  *= nums[i]

        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
    
    
#time 