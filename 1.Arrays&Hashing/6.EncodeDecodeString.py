#Encode and Decode Strings 
# LeetCode 271 
# Link: https://leetcode.com/problems/encode-and-decode-strings/ 

import string 
from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + '#' + s 
            # str is used to convert the length of the string to a string and then we concatenate it with '#' and the string itself
            # for example, if s = "hello", str(len(s)) + '#' + s = "5#hello"
            
        return result


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#': # finding the index of the '#' character
                j += 1
            
            length = int(s[i:j]) # converting the length of the string to an integer
            i = j + 1 # moving the index to the start of the string
            j = i + length # finding the end of the string
            result.append(s[i:j]) # adding the decoded string to the result list
            i = j

        return result # returns the list of decoded strings
      
      
# Time complexity: O(N) where N is the total length of the strings in the input list. The encode function iterates through each string in the list and concatenates the length of the string with the string itself. The decode function iterates through the encoded string and decodes each string. Both operations are linear in the length of the strings.

# The encode function iterates through each string in the input list and concatenates the length of the string with the string itself, separated by a '#' character. The resulting string is returned as the encoded representation of the input list of strings. The decode function reads the encoded string and extracts the length of each string and the corresponding substring. The decoded strings are stored in a list and returned as the result. 


