class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowDict = collections.defaultdict(set) # key will be the row index
        colDict = collections.defaultdict(set) # key will be the col index
        squareDict = collections.defaultdict(set) # key will be the [row//3, col//3]

        # Large matrix is broken down from row and col indexes ranging from 0-8 to 0-2
        # 0,0  0,1  0,2
        # 1,0  1,1  1,2
        # 2,0  2,1  2,2

        # Each 0-2 range has its accompaning larger matrix index values, gives us a key to store all the values that are in that
        # sub matrix
        # 0 = 0,1,2 // 3
        # 1 = 3,4,5 // 3
        # 2 = 6,7,8 // 3
 
        for r in range(9):

            for c in range(9):
                # if a "." is seen just continue next
                if board[r][c] == ".":
                    continue

                if (board[r][c] in rowDict[r] or
                    board[r][c] in colDict[c] or
                    board[r][c] in squareDict[r // 3, c // 3]):

                    return False
            

                # else add to the set 
                rowDict[r].add(board[r][c])
                colDict[c].add(board[r][c])
                squareDict[r // 3, c // 3].add(board[r][c])

            
        #print(rowDict)
        #print(colDict)
        #print(squareDict)

        # Nothing was flagged, return true meaning sodoku is valid
        return True