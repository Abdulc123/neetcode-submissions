public class Solution {
    public int Search(int[] nums, int target) {
        
        // Search through an array (sorted in ascending order) in O(logn) time
        // Return the targest location

        int L = 0;
        int R = nums.Length - 1;
        Console.WriteLine($"({L},{R})");


        while (L <= R)
        {
            int mid = (L + R ) / 2;
            int currentNum = nums[mid];
            Console.WriteLine($"({L},{R})");

            // if currentNum is less than target, search right half
            if (currentNum < target)
            {
                L = mid + 1;
            }
            // else if currentNum is greater than target, search left half
            else if (currentNum > target) 
            {
                R = mid - 1;
            }
            // else we found the currentNum 
            else
            {
                return mid;
            }
        }


        return -1; // Since not found


    }
}
