class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = x**2 + y**2

            heapq.heappush(heap, [-1 * dist, [x, y]])

            if len(heap) > k:
                heapq.heappop(heap)
            
        res = []
        for i in range(k):
            popped = heapq.heappop(heap)
            res.append(popped[1])
        return res
        

