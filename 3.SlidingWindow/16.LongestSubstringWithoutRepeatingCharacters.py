# leetcode link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        charset = set()
        l = 0
        res = 0

        for r in range(n):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1

            charset.add(s[r])

            res = max(r - l + 1, res)

        return res
    
    
    
    
