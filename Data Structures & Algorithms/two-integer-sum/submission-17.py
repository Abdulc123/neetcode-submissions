class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return the 2 indexes i,j so nums[i] + nums[j] == target  
        # Indexes i ~= j
        # Every solution has one correct solution pair i,j
        # Return answer with smallest index first


        index_dict: dict[int, int] = {}

        # Iterate over nums
            # At each num, check if you have seen its goal yet
                # if you have return the 2 index
        for j, num in enumerate(nums):
            goal = target - num
            if goal in index_dict:
                return [index_dict[goal], j]

            index_dict[num] = j
            
