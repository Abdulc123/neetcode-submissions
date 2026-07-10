class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # get the product of everything before and after the current number
        
        left_product = 1
        right_product = 1

        results = nums.copy()

        for i in range(len(nums)):
            left_product = 1
            right_product = 1
            
            for l in range(i):
                left_product *= nums[l]
            
            for r in range(i + 1, len(nums)):
                right_product *= nums[r]
            
            results[i] = left_product * right_product
        
        return results