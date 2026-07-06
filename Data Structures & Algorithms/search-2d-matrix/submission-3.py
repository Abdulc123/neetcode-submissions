class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # each row is in increasing order
        # first of every row  > last integer of previous row

        # Determine what row its in 
        # then find if its within that row, else return False
        nums = []
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            mid = (top + bot) // 2
            row = matrix[mid]


            # if target > max of row, move the top to be row + 1
            if target > row[-1]: 
                top = mid + 1
            elif target < row[0]:
                bot = mid - 1
            else:
                break # row is now the one containing the number maybe
            
        
        l, r = 0, len(row) - 1

        while l <= r:
            m = (l + r) // 2

            if target > row[m]:
                l = m + 1
            elif target < row[m]:
                r = m - 1
            else:
                return True # We found the number
        
        return False # if number is not found within the row 

        
        
                