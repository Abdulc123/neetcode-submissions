class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Return the k most frequent elements within an array

        # Create the frequency dict 
        freq_dict: dict[int, int] = {}
        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 0
            freq_dict[num] += 1
        
        print(freq_dict)
        
        # max_freq size = length of nums since thats the max amount of times a number could repeat
        freq_bucket: list[list[int]] = [[] for _ in range(len(nums) + 1)]

        result: list[int] = []

        # Store them in a list where the max size is the max frequency of a single thing
        for num, frequency in freq_dict.items():
            freq_bucket[frequency].append(num)
        
        # Iterate from right to left until result length == k
        for i in range(len(freq_bucket) - 1, -1, -1):
            bucket = freq_bucket[i]
            while bucket:
                result.append(bucket.pop())
                if len(result) == k:
                    return result
        
        return result