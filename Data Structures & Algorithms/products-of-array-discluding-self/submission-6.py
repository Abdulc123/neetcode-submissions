class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # get the product of everything before and after the current number
        
        n = len(nums)
        prefix_array = [1] * n
        suffix_array = [1] * n

        # 1  2  4 6
        # 1  1  2 8
        # 48 24 6 1
        results = nums.copy()

        # Calculate prefix array
        for i in range(n):
            if i == 0: 
                continue
            else:
                prefix_array[i] = prefix_array[i - 1] * nums[i - 1]
        
        # Calculate suffix array

        print(prefix_array)
        for r in range(n - 1, -1, -1):
            if r == n - 1:
                continue
            suffix_array[r] = suffix_array[r + 1] * nums[r + 1]

        results = [prefix_array[i] * suffix_array[i] for i in range(n)]
        print(suffix_array)

        return results
        

