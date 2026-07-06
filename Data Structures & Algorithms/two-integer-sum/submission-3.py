class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Create Dictionary to store value and index key value pair
        numIndexDict = {}

        # We can do this in one pass because once second element is seen 
        # the dictionary has all the elements to the left of it (including the
        # first one seen)
        for i, num in enumerate(nums):
            diff = target - num

            if diff in numIndexDict and i != numIndexDict[diff]:
                return [numIndexDict[diff], i] # return i second because that is the second element found
            else: # add the element to the dictionary
                numIndexDict[num] = i


        