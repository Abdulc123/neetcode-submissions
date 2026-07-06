class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        max_height = 0
        n = len(heights)
        # left and right pointers
        l = 0
  

        while l < n:
            r = n - 1

            while l < r:
                    # Calculations
                    area = min(heights[l], heights[r]) * (r - l)
                    max_area = max(area, max_area)

                    if heights[l] < heights[r]:
                        l += 1
                    else: 
                        r -= 1
            
            l += 1

        
        return max_area 
    




        
        