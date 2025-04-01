#leetcode link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0

        for i in range(0, n-1):
            buy = prices[i]
            print('i ', i, ' buy ', buy)

            for j in range(i, n):
                print('j ', j)
                print('prices[j] ', prices[j])
                pr = max(0, prices[j]- buy)
                profit = max(pr, profit)

        return profit

#This is a brute force solution, Time complexity: O(n^2) so not optimal and not recommended




#optimized solution using two pointer approach:
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

#Time complexity: O(n), Space complexity: O(1) but still not optimal


if __name__ == "__main__":
    solution = Solution()
    prices=[5,1,5,6,7,1,10]
    print(solution.maxProfit(prices))