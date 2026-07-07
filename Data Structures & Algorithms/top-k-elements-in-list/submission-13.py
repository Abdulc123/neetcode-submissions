from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = PriorityQueue()

        freq_dict: dict[int, int] = {}
        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 0
            freq_dict[num] += 1
        
        for num, freq in freq_dict.items():
            pq.put((-freq, num))
        
        result: list[int] = []

        while not pq.empty():
            if len(result) == k:
                return result
            result.append(pq.get()[1])
        
        return result
