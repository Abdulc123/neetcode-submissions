class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # two pointer approach
        # rebuild the list to include no spaces and only have alphabetic characteers

        stripped = "".join(char.lower() for char in s if char.isalnum())
        print(stripped)



        i = 0
        j = len(stripped) - 1

        while i < j:
            #print(stripped[i], stripped[j])
            if stripped[i] != stripped[j]:
                return False

            i += 1
            j -= 1
        
        return True