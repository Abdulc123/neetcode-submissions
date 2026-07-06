class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        countS = {}
        countT = {}

        # Base case
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        
        # Nothing is flagged so return True
        return countS == countT