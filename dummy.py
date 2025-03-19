from typing import List
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([i for i in s if i.isalnum()]).lower()
        return s == s[::-1]
        
        
if __name__ == "__main__":
    solution = Solution()
    input_str = "Was it a car or a cat I saw?"
    result = solution.isPalindrome(input_str)
    print(result)
    