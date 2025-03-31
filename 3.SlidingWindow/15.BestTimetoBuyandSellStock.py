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




if __name__ == "__main__":
    solution = Solution()
    prices=[5,1,5,6,7,1,10]
    print(solution.maxProfit(prices))