from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        l = 0
        r = len(heights) - 1
    
        while l<r:
            
            #print('[i] ', heights[i], ' [n-1-i] ', heights[n-1-i])
            
            h = min(heights[l], heights[r])
            w = r - l
            rest = h*w
            
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                # l += 1
                r -= 1
            # print('h ',h , ' w ', w, ' rest ', rest)
            res = max(res, rest)
    
        return res


if __name__ == "__main__":
    solution = Solution()
    heights = [1,7,2,5,4,7,3,6]
    print(solution.maxArea(heights))
    
    
    
    
    
    
