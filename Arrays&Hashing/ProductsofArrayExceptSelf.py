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
# The optimized approach uses two passes through the input list to calculate the product of all elements except the current element.
# The first pass calculates the product of all elements to the left of the current element, and the second pass calculates the product of all elements to the right of the current element.
# The final result is obtained by multiplying the left and right products for each element.
# The time complexity of this approach is O(N) where N is the length of the input list nums.
# The space complexity is O(N) as we use two additional lists to store the left and right products.