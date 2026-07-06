class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # If lengths are different, return false;
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}
        # Create a char : count dictionary for string 1
        for ltr in s:
            if ltr not in countS:
                countS[ltr] = 1
            else: # Car is in there so increase count by 1
                countS[ltr] += 1
        
        print(countS)

        for ltr in t:
            if ltr not in countT:
                countT[ltr] = 1
            else: # Car is in there so increase count by 1
                countT[ltr] += 1

        print(countS)

        return countS == countT

