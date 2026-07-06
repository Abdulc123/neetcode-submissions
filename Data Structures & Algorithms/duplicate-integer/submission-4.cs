public class Solution {
    public bool hasDuplicate(int[] nums) {
        // Create a dictionary to store the nums
        Dictionary<int, string> seenNums = new Dictionary<int, string>();

        // Iterate over the nums, 
        foreach (int num in nums) {
            Console.WriteLine(num);
            // If HashSet not empty and num in HashSet, return true
            if (seenNums.Count > 0 && seenNums.ContainsKey(num)) {
                return true;
            // Else: add to the hashset 
            } else {
                seenNums.Add(num, "In");
            }
        }

        // How to print out the dictionary
        foreach (var entry in seenNums) {
            Console.WriteLine($"Key: {entry.Key}, Value: {entry.Value}");
        }

        Console.WriteLine(seenNums);

        // When there are no duplicates return false
        return false; 
    }
}
