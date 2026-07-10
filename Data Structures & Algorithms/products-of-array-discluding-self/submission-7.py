class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # get the product of everything before and after the current number
        
        n = len(nums)
        prefix_array = [1] * n
        suffix_array = [1] * n

        # 1  2  4 6
        # 1  1  2 8
        # 48 24 6 1
        # Calculate prefix array
        for i in range(1, n):
            prefix_array[i] = prefix_array[i - 1] * nums[i - 1]
        
        # Calculate suffix array
        for r in range(n - 2, -1, -1):
            suffix_array[r] = suffix_array[r + 1] * nums[r + 1]

        results = [prefix_array[i] * suffix_array[i] for i in range(n)]

        return results
        

