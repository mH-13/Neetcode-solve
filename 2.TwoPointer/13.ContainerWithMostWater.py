#leetcode link: https://leetcode.com/problems/container-with-most-water/
#
# Problem: Container With Most Water
# Difficulty: Medium


#Brute force solution:

from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        

        for i in range(0, n - 1):
            l = 0
            r = len(heights) - 1
            # print('i ', i )
            
            for j in range(n-1, -1, -1):
                if i == j:
                    continue 
                
                h = min(heights[i], heights[j]) #height = [1,7,2,5,4,7,3,6]
                w = j - i
                rest = h*w
                # print('h ',h , ' w ', w, ' rest ', rest)
                res = max(res, rest)
            
        return res


if __name__ == "__main__":
    solution = Solution()
    heights = [1,7,2,5,4,7,3,6]
    print(solution.maxArea(heights))
    
#Time complexity: O(n^2) so not optimal and not recommended 


#optimized solution using two pointer approach: 



class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights) - 1
    
        while l<r:

            rest = min(heights[l], heights[r]) * (r - l)

            if rest> res:
                res = rest
            
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
    
        return res
      
      
#Time complexity: O(n) and space complexity: O(1) so this is optimal solution 