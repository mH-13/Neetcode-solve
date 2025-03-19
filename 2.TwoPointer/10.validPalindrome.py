#valid Palindrome

#Leetcode problem link: https://leetcode.com/problems/valid-palindrome/


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
    
    
#Time complexity: O(n)
#Space complexity: O(n)


#optimized solution using two pointer approach and isalphanum() function to check if the character is alphanumeric or not

from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            while l < r and not self.isalphanum(s[l]):
                l += 1
            while r > l and not self.isalphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True

        
    
    def isalphanum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))
        

if __name__ == "__main__":
    solution = Solution()
    input_str = "Was it a car or a cat I saw?"
    result = solution.isPalindrome(input_str)
    print(result)
    
#Time complexity: O(n)
#Space complexity: O(1)
#better than previous because we are not using extra space to store the new string
#we are using two pointer approach to solve the problem
#isalphanum() function is used to check if the character is alphanumeric or not
#ord() function is used to get the ASCII value of the character