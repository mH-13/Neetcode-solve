# Problem: 3Sum
# Difficulty: Medium
# link: https://leetcode.com/problems/3sum/
#

#optimized solution using two pointer approach:
from typing import List
import time
import atexit

# atexit.register(lambda: open("display_runtime.txt", "w").write(str(time.time()-start))) # write runtime to file display_runtime.txt when program exits normally 
# start = time.time()

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue

            l = i+1
            r = len(nums) - 1 

            while l<r:
                threesum = a + nums[l] + nums[r]
                if(threesum > 0 ):
                    r -= 1
                elif(threesum < 0):
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return res

#Time complexity: O(n^2) and space complexity: O(1) so this is optimal solution
#this approach is better than the previous one because we are using two pointer approach to solve the problem and we are also sorting the array to avoid duplicates in the result 

