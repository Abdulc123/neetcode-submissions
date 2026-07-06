public class Solution {
    public int[] ProductExceptSelf(int[] nums) {

        int[] result = new int[nums.Length];
        int leftProduct;
        int rightProduct;
        // Get the left and right products of the current i index and multiple them together, and write at position i
        for (int i = 0; i < nums.Length; i++)
        {
            leftProduct = 1;
            rightProduct = 1;

            for (int j = i - 1; j > -1; j-- )
            {
                leftProduct *= nums[j];
            }

            for (int k = i + 1; k < nums.Length; k++)
            {
                rightProduct *= nums[k];
            }

            result[i] = leftProduct * rightProduct;
        }        

        return result;
    }
}
