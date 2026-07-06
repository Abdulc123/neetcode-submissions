class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #have a list initalized at 1 and fill it with i's left product
        # [1,2,4,6]
        # [1,1,1,1]
        # [1,1,2,8]

        # lp = 1, L = 1, lp * 1 = 1
        # lp = 1, L = 1, lp * 2 = 2
        # lp = 2, L = 2, lp * 4 = 8
        # lp = 8, L = 8, lp * 6 = 48
        n = len(nums)
        leftList = [1 for i in range(n)]

        leftProduct = 1
        for i in range(n):
            leftList[i] = leftProduct
            leftProduct *= nums[i]
        
        #print(leftList)

        # [1,2,4,6]
        # [1,1,2,8]
        # [48, 24, 12, 8]

        # rp = 1, R = 8 * 1, rp  *= 6
        # rp = 6, R = 2 * 6, rp *= 4
        # rp = 24, R = 1 * 24, rp *= 2
        # rp = 48, R = 1 * 48
        rightProduct = 1
        for i in range(n-1, -1, -1):
            leftList[i] *= rightProduct
            rightProduct *= nums[i]
    
        return leftList