#twosum problem solution
#leetcode problem no 1
#link: https://leetcode.com/problems/two-sum/ 

def two_sum(nums, target):
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    return []
# Example usage:
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Indices of the two numbers that add up to {target}: {result}")
    # Output: Indices of the two numbers that add up to 9: [0, 1]

# This code defines a function `two_sum` that finds two indices in the list `nums` such that the numbers at those indices add up to `target`.
# It uses a dictionary to store the indices of the numbers as it iterates through the list, allowing for efficient lookups.
# The function returns a list of the two indices if a valid pair is found, or an empty list if no such pair exists.