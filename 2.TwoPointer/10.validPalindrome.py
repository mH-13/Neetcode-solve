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
        

#better than previous because we are not using extra space to store the new string
#we are using two pointer approach to solve the problem
#isalphanum() function is used to check if the character is alphanumeric or not
#ord() function is used to get the ASCII value of the character

#another apporach
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        s = s.lower()
        # count = 0

        while l <= r:
            
            # print(count)
            # print(s)
            if not ('a' <= s[l] <= 'z' or '0' <= s[l] <= '9'):
                # print(count, 's[l] ',s[l])
                l += 1
            elif not ('a' <= s[r] <= 'z' or '0' <= s[r] <= '9'):
                # print("s[r] ", s[r])
                r -= 1
            elif s[l] != s[r]:
                # print('s[l] - ' , s[l], 's[r]-',s[r])
                return False
            else: 
                l += 1 
                r -= 1
            # count += 1
        return True 
    
#Time complexity: O(n) here we are using only one while loop
#Space complexity: O(1) we are not using any extra space to store the new string
#using two pointer approach to solve the problem

#another approach
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([i for i in s if i.isalnum()]).lower()
        return s == s[::-1]
    
if __name__ == "__main__":
    solution = Solution()
    input_str = "Was it a car or a cat I saw?"
    result = solution.isPalindrome(input_str)
    print(result)
    
    

#Time complexity: O(n) 
#Space complexity: O(n)
#using list comprehension to get the alphanumeric characters from the string and converting it to lower case 
#comparing the string with the reverse of the string and returning True if the string is palindrome else False 