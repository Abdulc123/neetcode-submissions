public class Solution {
    public int LongestConsecutive(int[] nums) {
        
        int result = 0;
        HashSet<int> Set = new HashSet<int>(nums);

        // Sort the list O(n) time;
        Array.Sort(nums);

        foreach (int num in nums)
        {
            Console.Write($"{num} ");
        }

        // Then iterate through the list and when a value is found that is not a key, create a key, list[] entry for it
        for (int i = 0; i < nums.Length; i++)
        {
            if (!Set.Contains(nums[i] - 1)) {
                int count = 1;

                while (Set.Contains(nums[i] + count))
                {
                    count++;
                }
                result = Math.Max(result, count);
            }

        }

        return result;   
    }
}
