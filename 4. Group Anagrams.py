from typing import List
from collections import defaultdict

#solution 1
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for strng in strs:
            sortedS = ''.join(sorted(strng)) # sorted() returns a list of sorted characters in s and join() joins them back to a string 
            # print(sortedS) # aet -> aet, tea -> aet, eat -> aet  # sortedS is the key
            # print(res[sortedS]) # [] -> ['aet'] -> ['aet', 'tea'] -> ['aet', 'tea', 'eat']
            # print(res) # defaultdict(<class 'list'>, {'aet': ['aet', 'tea', 'eat']})
            # print(res.values()) # dict_values([['aet', 'tea', 'eat']])
            # print(list(res.values())) # [['aet', 'tea', 'eat']]
            
            result[sortedS].append(strng) # sortedS is the key and s is the value 
        return list(result.values()) # returns the values of the dictionary as a list 
    
# Time complexity: O(NKlogK) where N is the length of strs, and K is the maximum length of a string in strs. The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(KlogK) time.
# Space complexity: O(NK) where N is the length of strs, and K is the maximum length of a string in strs. The total information content stored in res is O(NK) because each string is stored once, and each string costs O(K) space.
# Runtime: 96 ms, faster than 97.68% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.3 MB, less than 99.67% of Python3 online submissions for Group Anagrams.
# Link: https://leetcode.com/problems/group-anagrams/


#solution 2
# Instead of sorting, we can use a tuple of 26 integers to represent the count of each character.  We can use this tuple as the key to the dictionary.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # defaultdict(<class 'list'>, {}) 
        
        for s in strs: # s = 'eat
            count = [0] * 26 # declaring a list of 26 zeros 
            
            for c in s:
                count[ord(c)- ord('a')] += 1 
                # ord('a') = 97, ord('b') = 98, ............ , ord('y') = 121, ord('z') = 122
                # print(count) # [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 
    
            res[tuple(count)].append(s) # tuple(count) is the key and s is the value 
            # print(res) # defaultdict(<class 'list'>, {(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1): ['eat']})
            # print(res.values()) # dict_values([['eat']])
            # print(list(res.values())) # [['eat']]
        
        return list(res.values()) # returns the values of the dictionary as a list
    
    
# Time complexity: O(NK) where N is the length of strs, and K is the maximum length of a string in strs. Counting each string is linear in the size of the string, and we count every string.
# Space complexity: O(NK) where N is the length of strs, and K is the maximum length of a string in strs. The total information content stored in res is O(NK) because each string is stored once, and each string costs O(K) space.
# Runtime: 88 ms, faster than 99.89% of Python3 online submissions for Group Anagrams.