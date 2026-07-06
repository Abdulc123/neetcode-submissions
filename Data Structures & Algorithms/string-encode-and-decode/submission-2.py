class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode the string to be like this:
        # "4&neet4&code4&love3&you"
        result = ""
        for string in strs:
            result += str(len(string)) + "&" + string
        
        return result
        

    def decode(self, s: str) -> List[str]:
        # identify the word and append it to result list based off count& identifier
        print(s)
        result = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "&":
                j += 1
            
            length = int(s[i:j]) # gives us the length up the upcoming list
            string = s[j + 1: j + length + 1] # gets the value after the & until the length of the string being searched for
            result.append(string)
            #print(string, i, j)

            i = j + length + 1
        
        return result

