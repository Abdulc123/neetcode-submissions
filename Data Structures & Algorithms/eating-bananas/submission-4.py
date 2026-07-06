class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles has x number of bananas in each ith pile
        # h is the number of hours to eat all the bannans in the piles
        # I can pick my bph eating rate as k
        # Each hour pick a pile of bannans and eat k bananas from that pile,
            # if pile has less than k bananas you cant go to another pile in that same hour 
        
        # Return minimum integer k so you can eat all the bananas within h hours

        # Get the max height since that would be max k
        # min k is always, 1
        # Do binary search 1 ... max piles, that value will equal result if the hours is less than h 
        # find the minimum k value result

        # Finding the max variable
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res





        
