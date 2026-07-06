public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        // Anagram is a string that has the same char frequency

        // Create dictionary to store a string as the key, and value is a list of strings
        var result = new Dictionary<string, List<string>>();

        // Iterate over each string in strs
        foreach (string str in strs) {
            // Populate arr of length 26, where index represents frequency of each letter
            // The index of a letter is letter - 'a' 
            // Ex. c = 50, a = 48, 50 - 48 = 2, index of c = 2 (0 indexed)
            int[] frequency = new int[26];
            // iterate over the str
            foreach (char s in str) {
                frequency[s - 'a'] += 1; // s - 'a' gives calculates the difference between for the index of the char
            }

            // Turn into a joined string
            string joinedKey = string.Join(',', frequency);
            // Console.WriteLine($"String: {str}, {joinedKey}");

            // If Dictionary does not contain key, then at the value create a list of strings
            if (!result.ContainsKey(joinedKey)) {
                result[joinedKey] = new List<string>(); // new list of strings initialized
            }

            // After Empty list bucket is created, add the string in there
            result[joinedKey].Add(str);
        }

        // foreach (var pair in result) {
        //     Console.Write($"{pair.Key}: ");
        //     foreach (string str in pair.Value) {
        //         Console.Write($" {str} ,");
        //     }
        // }
        

        // End Result: Return a list that groups anagrams together, list of lists(containing strings)
        return result.Values.ToList<List<string>>();
        // .Values gets the values from the results dictionary
    }
}
