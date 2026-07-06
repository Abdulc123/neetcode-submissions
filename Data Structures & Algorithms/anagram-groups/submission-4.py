class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        # Create a dictionary that has key of sorted(string)
        # value is the same strings when sorted
        asciiDict = defaultdict(list)
        for string in strs:
            key = ''.join(sorted(string)) # sorted the string, 
            # Else: it is in the Dict so append the string to it, default dict lets all keys default to an empty list
            asciiDict[key].append(string)

        return list(asciiDict.values())
        """

        # Create a dictionary to store counts of letters in strings as the key
        # value will be the correlating string appended to a list
        answerDict = defaultdict(list) # creates a dictionary where each value defaults to an empty list

        for s in strs:
            # default count to be letters a-z, through a list 0 - 25
            count = [0] * 26

            # for each letter in s
            for char in s:
                # append it in the count list at correct positions based off the ascii value - "a"
                count[ord(char) - ord('a')] += 1 # each index will be correlated with the count of specific letters and be unique only to strings that are angagrams
                # if ascii value of a = 35, 35 - 35 = 0, b = 36, 36 - 35 = 1, ...
        
            # if that count list converted to a tuple is found in answerDict, append the s string into as a value
            answerDict[tuple(count)].append(s)
        
        # return just the list of values in the dictionary as a list
        return list(answerDict.values())

