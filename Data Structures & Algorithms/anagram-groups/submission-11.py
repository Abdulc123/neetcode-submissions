class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each word
        # Have that be the key in the dict
        # The value will be the words that belong to that list

        groups: dict[str, list[str]] = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in groups:
                groups[sorted_word] = []

            groups[sorted_word].append(word)
        
        result: list[list[str]] = []
        for group in groups.values():
            result.append(group)
        
        return result
