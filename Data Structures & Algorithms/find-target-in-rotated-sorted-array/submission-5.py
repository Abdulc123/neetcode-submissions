class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Cases
            # 1. Midpoint is part of left and target is in right section
            # 2. Midpoint is part of left and target is in left section
            # 3. Midpoint is part of right and target is in left section
            # 4. Midpooint is part of right and target is in right section

        l, r = 0, len(nums) - 1

        while l <= r:

            m = (l + r) // 2
            # Find the target on the first try
            if nums[m] == target:
                return m

            # Check if we are in the left section for the mid point
            if nums[l] <= nums[m]:
                # If target is less than minimum, go to the right section
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else: # Search in the left section
                    r = m - 1

            else: # We are in the right section
                # If target is greater than max, go to the left section
                if target > nums[r] or target < nums[m] :
                    r = m - 1
                else: # Search in the right section
                    l = m + 1
                    
        return -1