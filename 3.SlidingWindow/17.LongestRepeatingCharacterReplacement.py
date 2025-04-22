#leetcode link: https://leetcode.com/problems/longest-repeating-character-replacement/

'''This is a variation of the above problem. The only difference is that we are allowed to replace k characters in the window to make all characters same.
The solution is almost same as above. The only difference is that we need to keep track of the character with maximum frequency in the window.
If the window size - max frequency > k, then we need to shrink the window.
The final answer is the maximum window size we have seen so far.'''

from typing import List


# brute force solution O(n^2)






class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]]) # max frequency of the character in the window
            # if the window size - max frequency > k, then we need to shrink the window

            while (r-l+1 )- max(count.values()) > k: # this is the only difference from the above problem is to check the max frequency of the character in the window
                # shrink the window and remove the leftmost character from the window 
                count[s[l]] -= 1
                l += 1
            
            res = max(res,r-l+1)

        return res

        