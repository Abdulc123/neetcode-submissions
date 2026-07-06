public class Solution {
    public bool hasDuplicate(int[] nums) {
        // Create a dictionary to store the nums
        HashSet<int> seenNums = new HashSet<int>();
        
        // Iterate over the nums, 
        foreach (int num in nums) {
            Console.WriteLine(num);
            // If HashSet not empty and num in HashSet, return true
            if (seenNums.Count > 0 && seenNums.Contains(num)) {
                return true;
            } else {
                seenNums.Add(num);
            }

            // Else add to the Hashset
            seenNums.Add(num);
        }

        // When there are no duplicates return false
        return false; 
    }
}
