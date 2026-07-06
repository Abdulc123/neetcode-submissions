public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {

        List<List<string>> result = new List<List<string>>();

        // Dictionary will store the anagrams, List of sorted chars and frequency : words that match
        Dictionary<string, List<string>> Groups = new Dictionary<string, List<string>>();    
        Dictionary<char, int> Frequency;

        foreach (string word in strs) 
        {
            // Generate the "Key" for the Groups based on letter frequency
            Frequency = new Dictionary<char, int>();
            foreach (char letter in word)
            {
                if (!Frequency.ContainsKey(letter)) 
                    Frequency.Add(letter, 0);
                
                Frequency[letter] += 1;
            }

            // Convert the frequency to a sorted string
            string FrequencyKey = string.Join(",", Frequency.OrderBy(pair => pair.Key).Select(pair => $"{pair.Key}:{pair.Value}"));

            // If the key does not exist in group, add the key alongside the word associated with it to the list
            if (!Groups.ContainsKey(FrequencyKey))
                Groups.Add(FrequencyKey, new List<string>());

            Groups[FrequencyKey].Add(word);
        }

        // Dictionary Printer
        Groups.ToList().ForEach(pair => Console.WriteLine($"{pair.Key} : {string.Join(",", pair.Value)}"));

        // Convert the Groups to a list
        result = Groups.Select(pair => pair.Value).ToList();

        return result;
        
    }
}
