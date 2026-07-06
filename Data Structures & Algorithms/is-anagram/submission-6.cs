public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) { // Base Case
            return false;
        }

        // Create dictionaries and populate them with char : count
        Dictionary<char, int> str1Dic = new Dictionary<char, int>();
        Dictionary<char, int> str2Dic = new Dictionary<char, int>();

        // Iterate over s, and count the number of times the character occurs
        for (int i = 0; i < s.Length; i++ ) {
            str1Dic[s[i]] = str1Dic.GetValueOrDefault(s[i], 0) + 1; // return count val if it exists, else it returns 0
            str2Dic[t[i]] = str2Dic.GetValueOrDefault(t[i], 0) + 1;
        }
        // 1. First ensure they have the same number of key value pairs
        // 2. str1Dic.Except(str2Dic) , returns the pairs in str1 that are not in str2 (A - B in Discrete math = x is an element in A that is not an element in B)
            // If except returns any pairs, that means there is a difference
            // .Any() checks for atleast one element, we do !.Any() to make sure there is no difference resulting from srt1.Except(str2);

        return str1Dic.Count == str2Dic.Count && !str1Dic.Except(str2Dic).Any();
    }
}
