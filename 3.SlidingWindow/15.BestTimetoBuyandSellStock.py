#leetcode link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        r = len(prices) - 1
        lftmx = 0
        rhsmn = float('inf')

        while l<r:
            if prices[l] < prices[r]:
                if prices[l] >= lftmx:
                    lftmx = prices[l]
                else:
                    res = max(res, lftmx - prices[l])
                l += 1
            else:
                if prices[r] <= rhsmn:
                    rhsmn = prices[r]
                else:
                    res = max(res, prices[r] - rhsmn)
                r -= 1
        return res

