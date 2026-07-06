public class Solution {

    public string Encode(IList<string> strs) {
        string result = "";
        
        foreach (string str in strs) {
            result += str.Length.ToString() + '%';
            foreach (char s in str) {
                result += s;
            }
        }

        Console.WriteLine(result);
        return result;
        // 4%neet4%code4%love3%you
    }

    public List<string> Decode(string s) {
        List<string> result = new List<string>();

        int i = 0;

        while (i < s.Length) {
            int j = i; // other traverser for string, helps capture the length of string
            //Console.WriteLine(s[i]);

            // Iterate until % is seen, j - i will be the number, -> convert to int
            while (j < s.Length && s[j] != '%') {
                j++;
            } // Now j is currently on a %

            // Substring gets the string within the index i to j
            // Converts subString to an int
            int length = int.Parse(s.Substring(i, j - i));
            i = j + 1;  // Move `i` past `%` to the start of the actual substring


            string subString = s.Substring(i, length);
            Console.WriteLine($"Length: {length}");
            Console.WriteLine($"Substring: {subString}");
            result.Add(subString);

            // Set j to right after the string ends
            i += length;  // Move `i` to the next encoded part (past the extracted substring)          

        }

        return result;
   }
}
