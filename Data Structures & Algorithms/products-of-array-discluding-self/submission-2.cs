public class Solution {
    public int[] ProductExceptSelf(int[] nums) {

        // Iterate over all the numbers and calculate the product of everything besides the current index

        int[] result = new int[nums.Length];
        for (int i = 0; i < nums.Length; i++) 
        {
            int leftProduct = 1;
            int rightProduct = 1;
            // Get the left product of it
            for (int j = 0; j < i; j++) 
            {
                leftProduct *= nums[j];
            }

            // Get the right product
            for (int k = i + 1; k < nums.Length; k++) 
            {
                rightProduct *= nums[k];
            }

            result[i] = leftProduct * rightProduct;
        }

    return result;
    }
}
