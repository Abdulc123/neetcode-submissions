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
                

        # Efficient Code using dictionary, enumerate, and diff
        numIndexDict = {}

        # Create dictionary where key = number, and value = the index it is at
        for index, num in enumerate(nums):
            numIndexDict[num] = index

        # Calculate the difference value and find the counter part index in the dictionary
        for index, num in enumerate(nums):
            difference = target - num

            if difference in numIndexDict and numIndexDict[difference] != index:
                return [index, numIndexDict[difference]]
        
