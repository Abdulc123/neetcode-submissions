class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram: string that contains the same exact characters as another string (order can be different)
        # same exact characters (same frequency count of chars)
        
        # create a frequency dict for string s
        if len(s) != len(t):
            return False

        s_frequency: dict[str, int] = {}
        t_frequency: dict[str, int] = {}


        for i in range(len(s)):
            s_frequency[s[i]] = 1 + s_frequency.get(s[i], 0)
            t_frequency[t[i]] = 1 + t_frequency.get(t[i], 0)
        
        return s_frequency == t_frequency