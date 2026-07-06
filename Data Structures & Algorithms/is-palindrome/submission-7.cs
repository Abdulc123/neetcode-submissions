public class Solution {
    public bool IsPalindrome(string s) {
        // Strip all spacing from the string
        // When iterating skip over any characters that are alphanumeric
        // make every letter lower case
        bool result = true;

        s = new string
        (
            s.Replace(" ", "")
            .ToLower()
            .Where(chr => char.IsLetterOrDigit(chr))
            .ToArray()
        );

        int L = 0;
        int R = s.Length - 1;
        Console.WriteLine(s);

        while (L <= R)
        {
            if (s[L] != s[R])
                return false;
            else
            {
                L++;
                R--;
            }
        }

        return result;
    }
}
