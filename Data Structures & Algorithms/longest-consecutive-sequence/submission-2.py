class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # return length of longest consecutive sequence of elements
        # valid sequence is when each next element is EXACTLY 1 greater than previous (does not have to be adjacent elements)
        # must be O(n) time, 

        # Create a numSet into a set
        numSet = set(nums)
        maxCount = 0
        
        # Iterate through the set
        for num in numSet:
            count = 0

            # Sequence start number is only valid, if number - 1 does not exist in the dictionary
            if (num - 1) not in numSet:
                count += 1

                # while number + 1, exists, increment count
                while (num + 1) in numSet:
                    count += 1
                    num += 1
        
            # established max count
            maxCount = max(maxCount, count)
       
        return maxCount 