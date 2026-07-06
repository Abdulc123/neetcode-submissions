public class Solution {
    public List<List<int>> ThreeSum(int[] nums) {
        
        // Set will capture the tuple of unique triplets, 
        // i,j,k must be unique
        // the triplet will contain the numbers at i,j,k that when added up equal 0

        HashSet<Tuple<int,int,int>> Set = new HashSet<Tuple<int,int,int>>();
        List<List<int>> result = new List<List<int>>();
        Array.Sort(nums);

        // Use i to iterate over the entire string
        for (int i = 0; i < nums.Length; i++) 
        {
            // j will be right after i, 
            for (int j = i + 1; j < nums.Length; j++)
            {
                // k will be right after j, 
                for (int k = j + 1; k < nums.Length; k++)
                {
                    if (nums[i] + nums[j] + nums[k] == 0) 
                    {
                        var Triplet = Tuple.Create(nums[i], nums[j], nums[k]);
                        Set.Add(Triplet);
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
