#leetcode link: https://leetcode.com/problems/valid-parentheses/

from  typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        p = {")" : "(", "}" : "{", "]" : "["}
        stack = []
        for i in range(n):
            if s[i] in p:
                # print('s[i] ', s[i])
                # print('p[s[i]] ', p[s[i]])
                # print('stack ', stack)
                # print('stack[-1] ', stack[-1])
                if stack and stack[-1] == p[s[i]]: #if stack is not empty and stack[-1] is equal to p[s[i]]
                    stack.pop()
                else:
                    return False
            else:
                # print('else : s[i] ', s[i])
                stack.append(s[i])
        
        return not stack

if __name__ == "__main__":
    solution = Solution()
    s="([{}])"
    print(solution.isValid(s))
    