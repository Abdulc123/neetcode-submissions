public class Solution {
    public int[] TwoSum(int[] numbers, int target) {

        // Numbers are sorted in increasing order, return the (1 indexed) of two indexes that add up to the given target
        // the two indexes can not be the same, index1 < index2, always one valid solution

        int[] result = new int[2];

        // Iterate over and find the pair of nums that satisfies above criteria
        for (int i = 0; i < numbers.Length - 1; i++) 
        {
            for (int j = i + 1; j < numbers.Length; j++)
            {
                // indexi < indexj
                // Look for two numbers that add up to the target
                if (numbers[i] + numbers[j] == target) 
                {
                    result = new int[] {i + 1, j + 1};
                }
            }
        }

        return result;
        
    }
}
