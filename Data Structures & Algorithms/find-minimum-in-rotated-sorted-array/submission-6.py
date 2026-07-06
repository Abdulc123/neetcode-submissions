class Solution:
    def findMin(self, nums: List[int]) -> int:

        n = len(nums)
        result = nums[0]
        l, r = 0, n - 1

        while l <= r:

            # Determine if array is already sorted:
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break
            
            # Determine whether the min is in the left or right based off midpoint
            m = (l + r) // 2
            result = min(result, nums[m]) 

            if nums[l] <= nums[m]: # It is in the right section
                l = m + 1
            else: # It is in the left section
                r = m - 1
            
        return result 


        

        