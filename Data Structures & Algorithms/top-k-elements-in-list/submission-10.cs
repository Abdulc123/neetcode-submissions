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


        // Create a Piority Queue (default its min heap) to store the (element, frequency)
        // We can turn it into a max heap by negating the frequencies
        PriorityQueue<int, int> maxHeap = new PriorityQueue<int, int>();
        foreach (var pair in frequencyDict) {
            maxHeap.Enqueue(pair.Key, -pair.Value);
        }

        // Console.WriteLine("Priority Queue");
        // while (maxHeap.Count > 0) {
        //     Console.WriteLine(maxHeap.Dequeue());
        // }

        // While there are stil k elements needed to be inserted
        for (int i = 0; i < k; i++) {
            // Dequeue from the max heap and store in the result list
            result[i] = maxHeap.Dequeue();
        }
    



        return result;
    }
}
