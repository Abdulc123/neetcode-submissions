public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int[] result = new int[nums.Length]; // creating an array with size nums
        int leftProduct = 1;
        int rightProduct = 1;

        for (int i = 0; i < nums.Length ; i++) {
            Console.WriteLine(nums[i]);
        
            // Get the product on the left side
            leftProduct = 1;
            for (int j = 0; j < i; j++) {
                leftProduct *= nums[j];
            }

            // Get the product on the right side
            rightProduct = 1;
            for (int k = i + 1; k < nums.Length; k++) {
                rightProduct *= nums[k];
            }

            result[i] = leftProduct * rightProduct;

        }


        return result;
    }


}
