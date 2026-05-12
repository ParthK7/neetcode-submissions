class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            dist = x**2 + y**2
            heapq.heappush(heap, [-1 * dist, i])
            if len(heap) > k:
                heapq.heappop(heap)
            
        res = []
        for i in range(k):
            _, index = heapq.heappop(heap)
            res.append(points[index])
        return res
        

