class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        # i + j = target
        for i in range(n):
            goal = target - nums[i]

            # look for goal in nums
            for j in range(i + 1, n):
                if nums[j] == goal and i != j:
                    return [i,j]
       


       # return nums[i] + nums[j] that = target, return i and j, i != j 


        