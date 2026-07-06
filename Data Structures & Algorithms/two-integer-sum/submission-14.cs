public class Solution {
    public int[] TwoSum(int[] nums, int target) {

        Dictionary<int, int> numIndex = new Dictionary<int, int>();
        // Iterate over nums and store them in a dictionary num:index
        for (int i = 0; i < nums.Length; i++) {
            numIndex[nums[i]] = i;
        }

        // Iterate over the nums again and search for its counterpart in the dictionary
        for (int i = 0; i < nums.Length; i++) {
            // Goal value = target - current num
            int goal = target - nums[i];

            // See if dictionary contains key goal, if so return the indices, else continue
            if (numIndex.ContainsKey(goal) && i != numIndex[goal]) { 
                return new int[] {i, numIndex[goal]};
            } 
        }

        return new int[0];
    
    }
}
