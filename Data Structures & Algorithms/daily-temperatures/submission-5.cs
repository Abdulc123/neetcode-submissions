public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        
        // result[i] = the number of days after the ith day before a warmer temperature appears. else it will be 0
        int[] result = new int[temperatures.Length];

        // Iterate through all the temps, i
        for (int i = 0; i < temperatures.Length; i++)
        {
            // For each of the j = i + 1 temps, iterate j up
            int j = i + 1;
            while (j < temperatures.Length)
            {
                // Break if the j temp is greater than i, meaning a warmer temp was found (count = j - i)
                if (temperatures[i] < temperatures[j])
                    break;
                else 
                    j++; // Look for the next temp 
                
            }
            
            // Set count to j - i, only if j < temperatures.Length - 1, else its 0
            int count = j < temperatures.Length ? j - i : 0;
            result[i] = count;

        }
        return result;
    }
}
