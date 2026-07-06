class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Iterate over all the strings in the list
        anagramDict = {} # hashed value : list of anagrams
        result = [] # a list of anagram lists 
        for word in strs:
            # Create a frequency dictionary, letter : count for each word
            freqDict = self.createFrequencyDict(word)
            print(freqDict)
            # Convert the word into something hashable (need to do this since dictionaries can't normally be hashed)
            hashedFrequency = self.hashFreqDict(freqDict)
            print(hashedFrequency)
        
            # Append to a temp dictionary hashed value : List of anagrams that have the same hash
            self.addToAnagramDict(anagramDict, hashedFrequency, word)

        # To our result list append the lists in the temp dictionary
        print(anagramDict)
        for hashKey, words in anagramDict.items():
            result.append(words)
            
        return result

    def createFrequencyDict(self, word):
        freqDict = {}
        for letter in sorted(word):
            if letter not in freqDict:
                freqDict[letter] = 1
            else: # we know its in there so increment by 1
                freqDict[letter] += 1
        return freqDict

    def hashFreqDict(self, freqDict):
        result = ""
        for letter, frequency in freqDict.items():
            result += f"{letter}:{frequency}"
        return result 
        
    def addToAnagramDict(self, anagramDict, hashedFrequency, word):
        if hashedFrequency not in anagramDict:
            anagramDict[hashedFrequency] = []
            anagramDict[hashedFrequency].append(word)
        else:
            anagramDict[hashedFrequency].append(word)
