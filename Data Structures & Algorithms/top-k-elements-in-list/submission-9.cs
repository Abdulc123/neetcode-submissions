public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        // Create result list
        int[] result = new int[k];
        
        // Create a Dictionary for to capture frequency and count num : count
        Dictionary<int, int> frequencyDict = new Dictionary<int, int>();

        // Iterate over nums and populate Dictionary
        foreach (int num in nums) {
            // Adds 1 to current value if it exists, 
            // Else it will add 1 to 0, (if num is not in Dict)
            frequencyDict[num] = 1 + frequencyDict.GetValueOrDefault(num, 0);
        }


        // Create an array that stores List<int> types similar to how int[] stores ints, where each index is a bucket of lists
        List<int>[] buckets = new List<int>[nums.Length + 1]; // each index is how many times the given numbers within the bucket repeat
        // (Note) Need to still initialize the lists before adding elements into them
        for (int i = 0; i < nums.Length + 1; i++) {
            buckets[i] = new List<int>(); // populates the array with newly initializes list that will store ints
        }

        // Nums with same frequency will be added to the same index buckets, iterate over key,value pairs in frequencyDict
        
        foreach (var pair in frequencyDict) {
            buckets[pair.Value].Add(pair.Key);
        }

        // Printing the contents of buckets
        for (int i = 0; i < buckets.Length; i++) {
            Console.Write($"[{i}] Entries:");
            // Iterate over each entry in list and print it out
            foreach (int n in buckets[i]) {
                Console.Write($" {n},");
            }
            Console.Write("\n");
            
        }

        // Iterate from right to left while the bucket is not empty
        int w = 0; // writing index for result array
        for (int i = buckets.Length - 1; i > 0; i--) {
            if (buckets[i].Any()) { // only when bucket has elements in it
                // while k > 0, add the right most values in the bucket into result
                foreach (int n in buckets[i]) {
                    if (k <= 0) break;
                    result[w++] = n;
                    k--;

                    if (k == 0) {
                        return result;
                    }
                }                
            }
        }



        return result;
    }
}
