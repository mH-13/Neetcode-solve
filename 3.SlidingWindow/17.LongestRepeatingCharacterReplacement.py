#leetcode link: https://leetcode.com/problems/longest-repeating-character-replacement/

'''This is a variation of the above problem. The only difference is that we are allowed to replace k characters in the window to make all characters same.
The solution is almost same as above. The only difference is that we need to keep track of the character with maximum frequency in the window.
If the window size - max frequency > k, then we need to shrink the window.
The final answer is the maximum window size we have seen so far.'''

from typing import List


# brute force solution O(n^2)

def characterReplacement(s: str, k: int) -> int:
  max_len = 0
  max_freq = 0
  count = {}
  left = 0

  for right in range(len(s)):
    count[s[right]] = count.get(s[right], 0) + 1
    max_freq = max(max_freq, count[s[right]])

    while (right - left + 1) - max_freq > k:
      count[s[left]] -= 1
      left += 1

    max_len = max(max_len, right - left + 1)

  return max_len