class TimeMap:


    def __init__(self):
        self.timeDict = defaultdict(list)
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Stores key with vlaue at the given timestamp
        # All calls to set are in increasing order
        
        self.timeDict[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        print(self.timeDict)
        # Returns most recent value of key, if its stored AND
        # most recent timstamp for that key prev_timestamp <= timestamp
        # if NO values, return ""
        res = ""
        values = self.timeDict.get(key, [])
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) //  2
            prevTimestamp = values[m][1]
            
            # if a vallue <= timestamp is found that is valid, continue searching for the largest or exact one that is <= timestamp
            if prevTimestamp <= timestamp:
                res = values[m][0]
                l = m + 1
                     
            # else it is not valid and look for something <=
            else:
                r = m - 1
        
        return res








