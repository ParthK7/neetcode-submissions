class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k

        self.nums = []

        for num in nums:
            heapq.heappush(self.nums, -1 * num)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -1 * val)

        array = []
        count = 0

        while count < self.k:
            count += 1

            array.append(heapq.heappop(self.nums))
        ans = -1 * array[-1]

        while array:
            heapq.heappush(self.nums, array.pop())
        return ans
        
