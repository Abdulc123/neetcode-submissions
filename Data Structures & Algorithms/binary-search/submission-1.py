class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        
        # if found return the index of the target
        while l <= r:
            mid = (l + r) // 2
            num = nums[mid]

            if num > target:
                r = mid - 1
            elif num < target:
                l = mid + 1
            else:
                return mid

        return -1
        