class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Create a val, count dict to store the elements:
        countDict = {}
        n = len(nums)
        for num in nums:
            countDict[num] = 1 + countDict.get(num, 0)

        # Initialize  to the length of nums, won't be using 0 so add + 1
        # to have the indexes represent possible number counts
        bucket_list = []
        for i in range(n + 1):
            bucket_list.append([])
            
        #print(countDict)

        # use s sort based where it has length(num), and
        # index = count, value is a list of how many numbers have the same count
        for num, count in countDict.items():
            bucket_list[count].append(num)

        # Iterate through  list, right to left, appending to answer k times
        # right most element of  is n 
        answer = []
        for i in range(n, 0, -1):
            # if the  has elements in it 
            for num in bucket_list[i]:
                answer.append(num)
                # if we reach k elements in answer, return answer
                if len(answer) == k:
                    return answer
