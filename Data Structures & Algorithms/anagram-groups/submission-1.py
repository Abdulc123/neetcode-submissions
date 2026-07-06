class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        answer = []

        # Create a dictionary that has key of sorted(string)
        # value is the same strings when sorted
        asciiDict = {}
        for string in strs:
            key = ''.join(sorted(string)) # sorted the string, 
            if key not in asciiDict:
                asciiDict[key] = [] # if it is not in Dict
            
            # Else: it is in the Dict so append the string to it
            asciiDict[key].append(string)

        print(asciiDict)
        # for each value (a list), append it to the answer
        for lst in asciiDict.values():
            answer.append(lst)


        return answer