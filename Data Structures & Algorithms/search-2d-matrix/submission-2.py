class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # each row is in increasing order
        # first of every row  > last integer of previous row

        # Determine what row its in 
        # then find if its within that row, else return False
        nums = []
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            row = (top + bot) // 2

            if target > matrix[row][-1]:  # if target is > top value of row
                top = row + 1
            elif target < matrix[row][0]: # if target is < bot value of row
                bot = row - 1
            else:
                nums = matrix[row]
                break
            
        
        l, r = 0, len(nums) - 1

        while l <= r and nums != []:
            m = (l + r) // 2

            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                return True # Found the number

        return False # Was unable to find the number

        
        
                