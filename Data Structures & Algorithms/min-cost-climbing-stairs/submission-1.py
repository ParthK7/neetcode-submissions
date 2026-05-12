class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}

        def dfs(index):
            if index in cache:
                return cache[index]

            if index >= len(cost):
                cache[index] = 0
                return 0

            ans = cost[index] + min(dfs(index + 1), dfs(index + 2))
            cache[index] = ans
            return ans
        
        return min(dfs(0), dfs(1))