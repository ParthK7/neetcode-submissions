class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = []

        for stone in stones:
            heapq.heappush(self.heap, -1 * stone)
        
        while len(self.heap) > 1:
            bigger = heapq.heappop(self.heap)
            smaller = heapq.heappop(self.heap)

            ans = bigger - smaller
            if ans != 0:
                heapq.heappush(self.heap, ans)

        if not self.heap:
            return 0
        return -1 * self.heap[0]