public class Solution {
    public List<List<int>> ThreeSum(int[] nums) {
        
        // Set will capture the tuple of unique triplets, 
        // i,j,k must be unique
        // the triplet will contain the numbers at i,j,k that when added up equal 0

        HashSet<Tuple<int,int,int>> Set = new HashSet<Tuple<int,int,int>>();
        List<List<int>> result = new List<List<int>>();
        Array.Sort(nums);

        foreach (int num in nums)
        {
            Console.Write($"{num}, ");
        }

        for (int i = 0; i < nums.Length; i++) {

            // Break if nums[i] is positive
            if (nums[i] > 0) break;

            // Break if nums[i] is the same as previous number (avoids repeats)
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            int target = -nums[i];
            int j = i + 1;
            int k = nums.Length - 1;

            while (j < k)
            {
                if (nums[j] + nums[k] < target)
                {
                    j++;
                }

                else if (nums[j] + nums[k] > target) 
                {
                    k--;
                }

                else {

                    // else the are equal so add them to thge Set
                    var tuple = Tuple.Create(nums[i], nums[j], nums[k]);
                    Set.Add(tuple);
                    // Move j, k to look for other possible triplets
                    j++;
                    k--;
                    
                    // Skip over duplicates
                    while (j < k && nums[j] == nums[j-1])
                    {
                        j++;
                    }
                }
            }
        }

        foreach (var tuple in Set) 
        {
            result.Add(new List<int> {tuple.Item1, tuple.Item2, tuple.Item3});
        }



        return result;


        
    }
}
