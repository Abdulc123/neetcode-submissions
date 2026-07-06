class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # return length of longest consecutive sequence of elements
        # valid sequence is when each next element is EXACTLY 1 greater than previous (does not have to be adjacent elements)
        # must be O(n) time, 

        # the start of a sequence means that n - 1 does not exist
        # 2,3,4,5 10 20

        max_count = 0

        nums = set(nums)

        for num in nums:
            count = 0
            if (num - 1) not in nums:
                count += 1
                # Find the consecutive numbers in the list 
                while (num + 1) in nums:
                    count += 1
                    num += 1
            
            # set the max count each time
            max_count = max(max_count, count)
        
        return max_count
                
                