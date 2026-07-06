class Solution:

    def encode(self, strs: List[str]) -> str:
        #encode the string with a unique identifier, length of word &
        result = ""
        for string in strs:
            result += str(len(string)) + "&" + string

        return result

    def decode(self, s: str) -> List[str]:
        # decode the string into a list 
        # 4&neet4&code4&love
        result = []

        i = 0
        n = len(s)

        while i < n - 1:
            j = i + 1
            # find where the count number ends
            while s[j] != "&" and j < n:
                j += 1
            
            length = int(s[i : j])
            result.append(s[j + 1: j + length + 1])
        
            i = j + length + 1

        return result


      

