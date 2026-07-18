class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if nums has no length return 0
        if not nums:
            return 0

        # turn answer into a set
        nums = set(sorted(nums))
        max_length = 0

        # Iterate over using for loop 
        for num in nums:
            # If num - 1 not in set -> starting a new sequence
            if num - 1 not in nums:

                curr = num
                while num + 1 in nums:
                    num = num + 1
                
                # We broke the consecutive sequence
                max_length = max(max_length, num - curr + 1)

        return max_length
