# Valid Sudoku
# LeetCode Problem: https://leetcode.com/problems/valid-sudoku/



from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set) #keys = (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in grid[(r//3, c//3)]:
                    return False 
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                grid[(r//3, c//3)].add(board[r][c])

        return True

# Time complexity: O(1) since the board is always 9x9. The space complexity is also O(1) since the size of the sets is constant.
# The algorithm uses three dictionaries to keep track of the numbers seen in each row, column, and 3x3 grid. It iterates through each cell in the board, checking if the number has already been seen in the corresponding row, column, or grid. If it has, the function returns False. If no duplicates are found, it returns True.
# The algorithm efficiently checks for duplicates in a Sudoku board by using sets to store the numbers seen in each row, column, and grid. The use of dictionaries allows for quick lookups and insertions, making the algorithm efficient and easy to understand.



        