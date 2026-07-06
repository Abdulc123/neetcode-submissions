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

        # create a dictionary with a key already initialized to an empty list
        groupDict = collections.defaultdict(list)

        for word in strs:

            count = [0] * 26
            # Create unique count key for the dictionary
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            # add key and element to the dict
            groupDict[tuple(count)].append(word)

        return groupDict.values()
        