from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        if n == 2:
            return max(0, prices[1] - prices[0])
        
        l = prices[0]
        r = prices[1]
        profit = 0
        for i in range(1, n-1):
            # print('outer i - ', i)
            print('l ', l, ' r ', r)
            
            pr = max(0, r - l)
            profit = max(profit, pr)
            
            if l >= r:
                # print('l ', l, ' r ', r)
                # print('i - ', i)
                l = r
                r = prices[i+1]              
            else:
                r = prices[i+1]
                
            pr = max(0, r - l)
            profit = max(profit, pr)
            
            # print('lastt l ', l, ' r ', r)
            # print('----------------------------------------------')
        return profit

if __name__ == "__main__":
    solution = Solution()
    prices=[1,2]
    # prices=[2,1,2,1,0,1,2]
    # prices=[7,1,5,3,6,4]
    print(solution.maxProfit(prices))
    
    
    
    
    
    
    
