class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # create a count dictionary with them
        numsCount = {}
        result = []
        n = len(nums)
        
        for num in nums:
            numsCount[num] = 1 + numsCount.get(num, 0)

        # create a bucket_sort list, n + 1 buckets, we dont use 0
        bucket = [[] for i in range(n + 1)]

        # index = number of times element repeats
        # value is a list containing the numbers that repeat
        for num, count in numsCount.items():
            bucket[count].append(num)
        
        print(bucket)

        # iterate over bucket from right to left until k elements have been added to result list
        for i in range(n, -1, -1):
            for num in bucket[i]:
                result.append(num)

                if len(result) == k:
                    return result
