class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = math.sqrt(x**2 + y**2)

            if len(heap) < k:
                heapq.heappush(heap, [-1 * dist, [x, y]])
            
            else:
                if -1 * heap[0][0] > dist:
                    heapq.heappop(heap)
                    heapq.heappush(heap, [-1 * dist, [x, y]])
            
        count = 0
        res = []

        while count < k:
            count += 1
            point = heapq.heappop(heap)
            res.append(point[1])
        return res

