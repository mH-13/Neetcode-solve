from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0
        r = 1
        profit = 0
        while r<=n-1:
            print('l ', l, ' r ', r, 'prices[l] ', prices[l], ' prices[r] ', prices[r])
            pr = max(0, prices[r] - prices[l])
            profit = max(profit, pr)
            
            if prices[l] > prices[r]:
                l+=1
                r += 1                
            else:
                r += 1
        return profit

if __name__ == "__main__":
    solution = Solution()
    # prices=[5,1,5,6,7,1,10]
    prices=[2,1,2,1,0,1,2]
    # prices=[7,1,5,3,6,4]
    print(solution.maxProfit(prices))
    
    
    
    
    
    
    
