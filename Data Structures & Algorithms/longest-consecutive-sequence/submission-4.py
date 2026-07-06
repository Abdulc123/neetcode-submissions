class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # !2 3 4 5 !10 !20
        # ! is the start of sequence since num - 1 does not exist

        container = set(nums)
        max_count = 0

        for num in container:
            count = 0
            # make sure its the start of a sequence
            if (num - 1) not in container:
                count += 1
                while num + 1 in container:
                    count += 1
                    num += 1

                max_count = max(max_count, count)

        #print(container)

        return max_count