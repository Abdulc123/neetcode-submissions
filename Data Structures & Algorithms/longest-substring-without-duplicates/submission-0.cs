public class Solution {
    public int LengthOfLongestSubstring(string s) {
        
        // Use a hashSet to store the letters,

        // Iterate over the the list with two pointers l and r
        // if r ever encounters a letter already contained within the window, shrink the window by l++ until everthing is unique
        
        int length = 0;
        int l = 0;
        int r = 0;
        HashSet<char> Set = new HashSet<char>();

        while (r < s.Length)
        {
            Console.WriteLine($"l = {l}:{s[l]} | r = {r}:{s[r]} | Length = {length} | {s.Substring(l, r - l + 1)}" );
            if (!Set.Contains(s[r]))
            {
                Set.Add(s[r]);
                length = Math.Max(length, r - l + 1);   
                r++;
            }
            else
            {
               Set.Remove(s[l]);
                l++;
            }
        }
        return length;
    }
}
