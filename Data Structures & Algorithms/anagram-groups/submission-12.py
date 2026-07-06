class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Iterate over all the words, 
            # create itsa frequency key list of [ints * 26] (frequencies of letters a-z)
            # use that as the key to the dict, this way (each word doesn't need to be sorted)

        groups: dict[str, list[str]] = {}
        for word in strs:
            frequency_key: list[int] = [0] * 26
            for ltr in word:
                frequency_key[ord(ltr) - ord('a')] += 1
            
            frequency_key = [str(num) for num in frequency_key]
            key = ",".join(frequency_key)
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        
        return [group for group in groups.values()]
            
