class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = x**2 + y**2

            heapq.heappush(heap, [-1 * dist, [x, y]])

            if len(heap) > k:
                heapq.heappop(heap)
            
        count = 0
        res = []

        while count < k:
            count += 1
            point = heapq.heappop(heap)
            res.append(point[1])
        return res

