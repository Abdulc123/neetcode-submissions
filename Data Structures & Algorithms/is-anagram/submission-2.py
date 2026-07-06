class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        base_dict = {}

        # Base case
        if len(s) != len(t):
            return False

        for letter in s:
            if letter not in base_dict:
                base_dict[letter] = 1
            else: 
                base_dict[letter] += 1
        
        print(base_dict)
        
        for letter in t:
            if letter not in base_dict:
                return False
            # if the letter is in there
            base_dict[letter] -= 1
            
            if base_dict[letter] < 0:
                #print("Letter",  letter)
                return False
            

        
        # Nothing is flagged so return True
        return True