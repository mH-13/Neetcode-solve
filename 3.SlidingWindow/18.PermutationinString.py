# Leetcode: https://leetcode.com/problems/permutation-in-string/

#

from typing import List
from collections import Counter

#brute force solution O(n^2)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)

        for i in range(len(s2)): 
            for j in range(i, len(s2)):
                newstr = s2[i:j+1] # substring of s2 and check if it is a permutation of s1 
                newstr = sorted(newstr)

                if newstr == s1: 
                    return True
        return False






def checkInclusion(s1: str, s2: str) -> bool:
  if len(s1) > len(s2):
    return False

  s1_count = Counter(s1)
  window_count = Counter(s2[:len(s1)])

  if s1_count == window_count:
    return True

  for i in range(len(s1), len(s2)):
    window_count[s2[i]] += 1
    window_count[s2[i - len(s1)]] -= 1

    if window_count[s2[i - len(s1)]] == 0:
      del window_count[s2[i - len(s1)]]

    if s1_count == window_count:
      return True

  return False