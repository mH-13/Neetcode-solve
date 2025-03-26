from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        p = {")" : "(", "}" : "{", "]" : "["}
        l = 0
        r = n-1
        c = 0
        while l<r:
            if(s[l] != p[s[r]]):
                return False
            else:
                # print('s[l] ', s[l], ' p[s[r]] ', p[s[r]], 'c ', c)
                c += 1
                l += 1
                r -= 1
        if c == n /2:
            return True
        else:
            # print('c ', c, 'n ', n)
            return False


if __name__ == "__main__":
    solution = Solution()
    s="()[]{}"
    print(solution.isValid(s))
    
    
    
    
    
    
    
