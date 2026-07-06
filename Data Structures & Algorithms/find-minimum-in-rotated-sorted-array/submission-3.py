class Solution:
    def findMin(self, nums: List[int]) -> int:
        # determine the middle number
        # find the smallest number to the left and right of it, return the smallest number amongst the three

        n = len(nums)
        result = nums[0]
        # Determining the middle number
        l, r = 0, n - 1

        while l <= r:
            # Check if we are in sorted format initially, if so return the left most pointer
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break

            # Binary search on left or right side
            m = (l + r) // 2
            result = min(result, nums[m])
            if nums[l] <= nums[m]: # Check the right side of the array
                l = m + 1
            else: # Check the left side of the array
                r = m - 1
            print(nums[l:r + 1], result)
        
        return result

        

        