class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Create the empty dictionary
        numIndexDict = {}

        # Fil in dictionary with num, index value pair, (can be done while creating the dictionary)
        for i, num in enumerate(nums):
            diff = target - num
            # When difference is seen, return the found i, and difference
            if diff in numIndexDict:
                return [numIndexDict[diff], i]

            numIndexDict[num] = i


        