import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for num in nums:
            m[num] = m.get(num, 0) + 1
        
        h = [(-freq, num) for num, freq in m.items()]
        heapq.heapify(h)

        return [heapq.heappop(h)[1] for _ in range(k)]