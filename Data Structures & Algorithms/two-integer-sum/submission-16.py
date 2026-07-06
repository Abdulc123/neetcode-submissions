class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return the 2 indexes i,j so nums[i] + nums[j] == target  
        # Indexes i ~= j
        # Every solution has one correct solution pair i,j
        # Return answer with smallest index first

        for i in range(len(nums)):
            print(f"i = {nums[i]}")
            for j in range(i + 1, len(nums)):
                print(f"j = {nums[j]}")
                if nums[i] + nums[j] == target:
                    return [i, j]
