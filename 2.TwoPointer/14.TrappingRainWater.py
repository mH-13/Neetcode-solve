#leetcode link: https://leetcode.com/problems/trapping-rain-water/
# #
# # Problem: Trapping Rain Water
# # Difficulty: Hard

#fist solution with O(n) time complexity and O(n) space complexity
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        minlr = [0] * len(height)

        lftmx = 0
        rhsmx = 0
        for i in range(0, len(height)-1):
            lftmx = max(lftmx, height[i])
            left_max[i] = lftmx

        for i in range(len(height)-1,-1,-1):

            rhsmx = max(rhsmx, height[i])
            right_max[i] = rhsmx
        
        for i in range(0, len(height)):
            minlr[i] = min(left_max[i], right_max[i])

        for i in range(0, len(height)-1):
            total += max(0, minlr[i] - height[i])

        return total

#Time complexity: O(n) and space complexity: O(n) so this is optimal solution 