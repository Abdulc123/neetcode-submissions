class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Return true if a number appears more than once

        # Create a set to store numbers seen
        nums_seen: set = set()
        # Iterate over the numbers, new number means add it to set
        for num in nums:
            # if number is already in set, return false
            if num not in nums_seen:
                nums_seen.add(num)
            else:
                return True

        return False
        