public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {

        // Create a dictionary to capture the frequency of each number
        Dictionary<int, int> frequency = new Dictionary<int, int>();
        PriorityQueue<int, int> maxPQ = new PriorityQueue<int,int>();
        int[] result = new int[k];

        for (int i = 0; i < nums.Length; i++) 
        {
            // number : frequency
            if (!frequency.ContainsKey(nums[i]))
            {
                frequency.Add(nums[i], 0);
            }

            // If it is in the dict, increment its count:
            frequency[nums[i]] += 1;
        }

        // Create a PriorityQueue and populate it with the number as the element, and the priority as the count
        
        foreach (var pair in frequency)
        {
            maxPQ.Enqueue(pair.Key, -pair.Value); // make it negative since its a minHeap by default
        }

        for (int i = 0; i < k; i++)
        {
            result[i] = maxPQ.Dequeue();
        }

        // while (maxPQ.Count > 0)
        // {
        //     int maxElement = maxPQ.Dequeue();
        //     Console.WriteLine($"Num: {maxElement}");
        // }
        

        return result;
    }
}
