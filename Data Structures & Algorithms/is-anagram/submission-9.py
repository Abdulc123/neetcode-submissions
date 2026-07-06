class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram: string that contains the same exact characters as another string (order can be different)
        # same exact characters (same frequency count of chars)
        
        # create a frequency dict for string s
        s_frequency: dict[str, int] = {}
        for ltr in s:
            if ltr not in s_frequency:
                s_frequency[ltr] = 1
            else:
                s_frequency[ltr] += 1
        
        print(s_frequency)

        # iterate over t
        for ltr in t:
            # each letter seen means subtracting 1 from s frequency dict
            if ltr not in s_frequency:
                return False
            s_frequency[ltr] -= 1
        
        print(s_frequency)
        # check if all letters in frequncy dict are all 0, if not then we return false
        for v in s_frequency.values():
            if v != 0:
                return False

        return True
