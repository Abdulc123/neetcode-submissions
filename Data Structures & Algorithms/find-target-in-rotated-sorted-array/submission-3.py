class Solution:
    def search(self, nums: List[int], target: int) -> int:


        l, r = 0, len(nums) - 1

        while l <= r:

            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            print(l,m,r)
        
            # Check if we are in the left section:
            if nums[l] <= nums[m]: 
                # If target is less than min value (left value) go to right side, or target greater than whats at mid point
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else: # Target is within the left section
                    r = m - 1

            # We are in the Right Section
            else:
                # If target is greater than max of right side (right value) go to the the left side, or target  LT whats at midpoint
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else: # Target is witihn the right section
                    l = m + 1
        
        return -1