
from typing import List

#initial approach - O(n^2)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        lst = set(nums)
        for n in nums:
            strek = 0
            curr = n
            while curr in lst:
                strek += 1
                curr +=1

            res = max(res, strek)
        return res
    
# Time complexity: O(n^2) where n is the length of the input list nums. The outer loop iterates through each element in the list, and the inner loop checks for consecutive elements. This results in a quadratic time complexity.