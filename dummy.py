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

        for i in range(len(height)-1,-1,-1): # to fix this line of code we need to change the range to len(height)-1, -1, -1  and also change the range of the for loop to 0, len(height)-1

            rhsmx = max(rhsmx, height[i])
            right_max[i] = rhsmx
        
        for i in range(0, len(height)):
            minlr[i] = min(left_max[i], right_max[i])
            
        print('left_max:', left_max)
        print('right_max:', right_max)
        print('minlr:', minlr)

            

        

        


if __name__ == "__main__":
    solution = Solution()
    height = [0,2,0,3,1,0,1,3,2,1]
    solution.trap(height)
    
    
    
    
    
    
    
