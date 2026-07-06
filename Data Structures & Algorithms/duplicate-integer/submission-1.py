class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsDic = {}

         # Check if num in ditionary
        for num in nums:
            if num in numsDic:
                return True

            # else add it to dictionary
            numsDic[num] = 1
        

        return False