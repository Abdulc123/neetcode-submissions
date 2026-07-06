class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # array is sorted increasing order
        # return 1 indexed soltiion of i1 and i2 so they ad up to the target
        # i1 < i2

        n = len(numbers)
        l = 0
        r = n - 1

        while l < r:
            
            # have the value
            value = numbers[l] + numbers[r]

            if value > target:
                r -= 1
            elif value < target: 
                l += 1
            else: # we found the target
                return [l + 1, r + 1]

            

        