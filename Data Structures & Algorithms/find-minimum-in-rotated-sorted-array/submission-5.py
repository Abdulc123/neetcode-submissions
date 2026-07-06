class Solution:
    def findMin(self, nums: List[int]) -> int:

        n = len(nums)
        result = nums[0]
        l, r = 0, n - 1

        while l <= r:
            # If its already sorted the left most elmenet is the result
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break

            # When it is rotated
            m = (l + r) // 2
            result = min(result, nums[m])

            if nums[l] <= nums[m]: # Mid is part of the left section
                l = m + 1
            else: # Mid is part of the right section 
                r = m - 1
        
        return result


        

        