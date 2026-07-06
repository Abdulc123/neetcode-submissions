class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # each row is in increasing order
        # first of every row  > last integer of previous row

        # Determine what row its in 
        # then find if its within that row, else return False
        nums = []
        for row in matrix:
            # if target is less than the max of the row, it should be in that row
            if target <= row[-1]:
                nums = row
                break
        
        if nums == []:
            return False
            
        
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                return True # Found the number

        return False # Was unable to find the number

        
        
                