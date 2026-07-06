class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Create a val, count dict to store the elements:
        countDict = {}
        n = len(nums)
        for num in nums:
            countDict[num] = 1 + countDict.get(num, 0)

        # Initialize bucket to the length of nums, won't be using 0 so add + 1
        # to have the indexes represent possible number counts
        bucket_list = []
        for i in range(n + 1):
            bucket_list.append([])
            
        #print(countDict)

        # use buckets sort based where it has length(num), and
        # index = count, value is a list of how many numbers have the same count
        for num, count in countDict.items():
            bucket_list[count].append(num)

        print(bucket_list)
        # Iterate through bucket list, right to left, appending to answer k times
        # right most element of bucket is n - 1
        
        answer = []
        for i in range(n, -1, -1):
            # if the bucket has elements in it 
            if bucket_list[i] != []:
                # while the bucket is not empty and k elements should still be added
                while k != 0 and len(bucket_list[i]) != 0:
                    answer.append(bucket_list[i].pop())
                    k -= 1

            if k == 0:
                return answer


        #return answer