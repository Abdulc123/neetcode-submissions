public class Solution {
    public int Search(int[] nums, int target) {

        int l = 0;
        int r = nums.Length - 1;

        while (l <= r)
        {
            int mid = (l + r) / 2;
            Console.WriteLine($"l = {l} | m = {mid} | r = {r}");

            if (nums[mid] < target)
                l = mid + 1;
            else if (nums[mid] > target)
                r = mid - 1;
            else
                return mid;
        }
        

        // Not found so return -1
        return -1;
    }
}
