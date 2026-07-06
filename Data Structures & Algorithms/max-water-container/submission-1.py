class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        

        maxWater = 0

        for l in range(n):
            r = n - 1
            while l <= r:
                water = min(heights[l], heights[r]) * (r - l)
                maxWater = max(water, maxWater)
                r -= 1

        
        return maxWater
        