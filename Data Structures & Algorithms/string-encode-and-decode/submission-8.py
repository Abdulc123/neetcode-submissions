class Solution:

    def encode(self, strs: List[str]) -> str:
        # get the length of the word
        # put a seperator (lets do $)
        # send that string back over
        string: str = ""
        for word in strs:
            length = len(word)
            string += f"{length}${word}"
        return string 


    def decode(self, s: str) -> List[str]:
        print(s)
        # read strings until we reach special delimiter
        # everything before delimiter is a number (length of our word)
        # Read x amount of letters after delimeter and place that in our list
        result: List[str] = []
        i = 0
        while i < len(s):

            j = i
            while j < len(s):
                current = s[j]
                if current == "$":
                    break
                j += 1
            
            # We break out of loop and now j is sitting on $
            num_string = s[i:j]

            # convert num string into a num:
            try:
                word_length = int(num_string)
            except ValueError as e:
                print(f"Unable to convert {num_string} to an integer {e}")


            # Set i = the start of the next number
            i = j + word_length + 1

            # The word starts at j + 1 and ends at the new i
            word = s[j + 1: i]
            result.append(word)

        return result
