public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        var result = new int[2];

        // Sorted in increasing order
        int L = 0;
        int R = numbers.Length - 1;

        int sum = 0;
        while (L <= R)
        {
            sum = numbers[L] + numbers[R];
            if (sum > target)
                R--;
            else if (sum < target)
                L++;
            else // They are equal
            {
                result[0] = L + 1;
                result[1] = R + 1;
                break;
            }
        }
        
        return result;


        // Return 1 index of two numbers [index1, index2]
        // index1 < index2
        // index1 != index2
        // Always one exact valid solution 
    }
}
