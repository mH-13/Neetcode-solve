# Problem: 167. Two Sum II - Input array is sorted
# Difficulty: Easy
#link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/



from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sum =0
        res = []
        leng = len(numbers)
        for n in range(0, leng):
            for j in range(0, leng):
                if n != j:
                    # print(n, j)
                    sum = numbers[n] + numbers[j]
                    # print("sum", sum)
                    if sum == target:
                        res.extend([n+1, j+1])
            if res:
                return res
        
if __name__ == "__main__":
    solution = Solution()
    numbers=[-5,-3,0,2,4,6,8]
    target=5
    print(solution.twoSum(numbers, target))
    
#Time complexity: O(n^2) so not optimal and not recommended


#optimized solution using two pointer approach:
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        res = []

        while l<r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                res.extend([l+1, r+1])
                return res
#Time complexity: O(n) and space complexity: O(1) so this is optimal solution
#this approach is better than the previous one because we are using two pointer approach to solve the problem