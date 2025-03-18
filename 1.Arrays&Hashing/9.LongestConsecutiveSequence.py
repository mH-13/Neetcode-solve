
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