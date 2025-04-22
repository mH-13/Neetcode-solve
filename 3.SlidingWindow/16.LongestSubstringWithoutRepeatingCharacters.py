# leetcode link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# This is a classic sliding window problem. The idea is to use two pointers to create a window that can expand and contract as needed.
# The left pointer represents the start of the window, and the right pointer represents the end of the window.
# We will use a set to keep track of the characters in the current window. If we encounter a character that is already in the set, we will move the left pointer to the right until we remove the duplicate character from the set.
# The time complexity of this algorithm is O(n), where n is the length of the input string. This is because we are iterating through the string once with the right pointer and at most once with the left pointer.
# The algorithm uses a set to keep track of the characters in the current window. It iterates through the string with the right pointer, adding characters to the set. If a duplicate character is found, it moves the left pointer to the right until the duplicate is removed from the set. The maximum length of the substring without repeating characters is updated as needed.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        charset = set() # to store the characters in the current window
        l = 0
        res = 0

        for r in range(n): # r is the right pointer
            # if s[r] is already in the set, we need to move the left pointer to the right until we remove the duplicate character from the set
            while s[r] in charset:
                charset.remove(s[l])
                l += 1

            charset.add(s[r]) # add the current character to the set

            res = max(r - l + 1, res) # update the maximum length of the substring without repeating characters
        
        # return the maximum length of the substring without repeating characters
        return res
    
    
    
    
