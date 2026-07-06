class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        for string in strs:

            for char in string:
                encoded_string.append(str(ord(char)))
                encoded_string.append('A')
            encoded_string.append('B')
        
        return "".join(encoded_string)
        

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        words = s.strip().split('B')
        words.pop()
        #print(words)

        for wrd in words:
            characters = wrd.strip().split('A')
            characters.pop()
            #print(characters)
            
            result = []
            for char in characters:
                result.append(chr(int(char)))

            decoded_list.append("".join(result))

        return decoded_list
