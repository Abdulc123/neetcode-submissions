class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Create dictionary to store values
        numDict = {}

        # Add in values, [num: index]
        for i, num in enumerate(nums):
            numDict[num] = i

        # Iterate through nums and look for the target - val aka goal
        for i in range(len(nums)):
            goal = target - nums[i]

            if goal in numDict and i != numDict[goal]:
                return [i, numDict[goal]]




        