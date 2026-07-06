class Solution:

    def encode(self, strs: List[str]) -> str:
        # Given words in a list
        # combine the words into a single string that can be decoded
        # length of word, symbol, word 
        result = ""
        for word in strs:
            result += str(len(word)) + "$" + word
        print(result)
        return result
        

    def decode(self, s: str) -> List[str]:
        #4$neet4$code4$love3$you
        result = []
        n = len(s)
        i = 0
        while i < n:
            j = i

            # find the length of the count
            while j < n and s[j] != "$":
                j += 1
        
            length = int(s[i:j])
            # start at the first letter
            i = j + 1
            print(s[i: i + length])
            result.append(s[i: i + length])
            i = i + length
            
        return result


      

