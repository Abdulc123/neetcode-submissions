class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numIndex = {} # num : index
        n = len(nums)

        # Iterate over nums list and store the index where each num is located
        for i, num in enumerate(nums):
            numIndex[num] = i
        

        # Iterate over numbers in num, to find the goal at each num
        for i in range(n):
            # Compute the goal = target - current num
            goal = target - nums[i]

            # Look for goal in numIndex, once found return [i, j], and i != j 
            if goal in numIndex and i != numIndex[goal]:
                return[ i , numIndex[goal]]






        