class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return indices i and j where
            # nums[i] + nums[j] == target
            # i != j
        
        # #O(n^2) approach, brute force:
        # n = len(nums)
        # for i in range(n):
        #     for j in range(1, n):
        #         if nums[i] + nums[j] == target and i != j:
        #             return [i , j]
                

        numIndexDict = {}

        for i, num in enumerate(nums):
            diff = target - num # looking for this value
    
            if diff in numIndexDict and numIndexDict[diff] != i:
                return [numIndexDict[diff], i]
            
            numIndexDict[num] = i
        
        print(numsIndexDict)