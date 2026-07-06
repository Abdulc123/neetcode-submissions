public class Solution {
    public int MaxArea(int[] heights) {
        // Return the maximum amount of water a container can store
        // Max Water = distance between containers and the max height between the two
        // Use i to iterate over each bar
        // j moves from right to left, skipping if the height of the next column is smaller than previous (since the width just shrunk)
        // so it will never be greater

        int maxArea = 0;
        int maxHeight = 0;

        int l = 0;
        int r = heights.Length - 1;

        while (l < r)
        {
            int area = (r - l) * Math.Min(heights[l], heights[r]);
            maxArea = Math.Max(maxArea, area);
            
            // Move the pillar that has the smallest height (to avoid wasting time checking pillars we know will not be correct)
            if (heights[l] <= heights[r])
                l++;
            else
                r--;


            Console.WriteLine($"{l}, {r}: Area = {area}");
        }

        return maxArea;
    }
}
