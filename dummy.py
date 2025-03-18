
from typing import List
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        
        for c in s:
            if c.isalnum():
                newstr += c.lower()
                
            return newstr == newstr[::-1]
        
if __name__ == "__main__":
    solution = Solution()
    input_str = "Was it a car or a cat I saw?"
    result = solution.isPalindrome(input_str)
    print(result)