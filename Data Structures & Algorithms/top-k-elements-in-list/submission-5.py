class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Create a val dictionary to count number of times num appears in list
        countDict = {}
        for i, num in enumerate(nums):
            countDict[num] = 1 + countDict.get(num, 0)
        
        answer = []
        #print(countDict)

        # Create a bucket list based on the length of nums, each index represents how many times a number repeats
        # do n + 1 do make sure the index correlates with count (stops list from starting at 0 and ending at n-1)
        n = len(nums)
        bucketList = [[] for i in range(n + 1)]
        #print(bucketList)

        # for each num, count in the dictionary, organize them in the buckets
        # based on the count, that will be the index it is stored in the buckets
        for num, count in countDict.items():
            bucketList[count].append(num)

        print(bucketList)

        # Read the buckets from right to left to append the k most frequent elments to answer
        # stop when len(answer) == k
        for i in range(n, -1, -1):
            for num in bucketList[i]:
                answer.append(num)
                if len(answer) == k:
                    return answer
 
