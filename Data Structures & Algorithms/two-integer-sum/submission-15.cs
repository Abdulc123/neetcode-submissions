public class Solution {
    public int[] TwoSum(int[] nums, int target) {

        // Create a dictionary to store num:index
        Dictionary<int, int> numIndex = new Dictionary<int, int>();

        // Iterate over nums and populate dictionary
        for (int i = 0; i < nums.Length; i++) {
            numIndex[nums[i]] = i;
        }

        // Printing out dictionary
        // foreach (var pair in numIndex) {
        //     Console.WriteLine($"Num: {pair.Key}, Index: {pair.Value}");
        // }
        
        // Iterate over nums and for each num: goal = target - current num
        for (int i = 0; i < nums.Length; i++) {
            int goal = target - nums[i];
            // If Goal in Dictionary and goal_index != i: return i,j
            if (numIndex.ContainsKey(goal) && numIndex[goal] != i) {
                return new int[]{i, numIndex[goal]};
            }
                
        }

        // Return [0,0] if nothing found
        return new int[0];
    }
}
