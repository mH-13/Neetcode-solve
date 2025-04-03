#leetcode link: https://leetcode.com/problems/longest-repeating-character-replacement/
'''This is a variation of the above problem. The only difference is that we are allowed to replace k characters in the window to make all characters same.
The solution is almost same as above. The only difference is that we need to keep track of the character with maximum frequency in the window.
If the window size - max frequency > k, then we need to shrink the window.
The final answer is the maximum window size we have seen so far.'''

from typing import List


# brute force solution O(n^2)

