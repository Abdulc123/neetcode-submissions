public class Solution {
    public int MinEatingSpeed(int[] piles, int h) {
        
        // Index i is the ith pile, where piles[i] is how many bananas are in that pile
        // h represents the number of hours you have to eat all the bananas

        // User can decide number of bph (banans per hour) as rate = k
        // Choose a pile of bananas and eat k bananas from that pile, if pile has less than k bananas, you can finish eating pile but 
        // CANT move one. 

        // Return the minimum integer k rate(bph) that you can eat all the bananas within h hours

        // The max rate you can eat at is the largest pile number (can have higher but no point)
        // Smallest rate you can eat at is 1; (It will take a while but could possible have hoursTaken < h)
        // Hours taken = Ceiling(pile of bananas / k)


        int hoursTaken;

        int l = 1;
        int r = piles.Max();
        int smallestK = r;

        while (l <= r)
        {
            int mid = (l + r) / 2;
            hoursTaken = CalculateHoursAtRate(mid, piles);

            if (hoursTaken > h)     
                l = mid + 1;
            else if (hoursTaken <= h)
            {
                smallestK = Math.Min(smallestK, mid);
                Console.WriteLine($"Smallest K Rate = {smallestK} with {hoursTaken} hours taken | Mid = {mid}");
                r = mid - 1;   
            }
        }

        return smallestK;
    }

    int CalculateHoursAtRate(int k, int[] piles)
    {
        int hoursTaken = 0;
        for (int i = 0; i < piles.Length; i++)
        {
            hoursTaken += (int)Math.Ceiling((double)piles[i] / k);
        }

        return hoursTaken;
    }
}
