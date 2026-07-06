class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # each row and column must have digits 1-9, without diplicates
        # each 3x3 sub matrix should not have duplicates within it
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        box_dict = defaultdict(set)

        for r in range(9):
            for c in range(9):
                # Only numbers should be included
                if board[r][c] == '.':
                    continue
                # Check for dupes:
                if (board[r][c] in row_dict[r] or 
                    board[r][c] in col_dict[c] or
                    board[r][c] in box_dict[r//3, c//3]):
                    print(board[r][c])
                    return False
                else:
                    row_dict[r].add(board[r][c])
                    col_dict[c].add(board[r][c])
                    box_dict[r // 3, c // 3].add(board[r][c])

        
        return True
