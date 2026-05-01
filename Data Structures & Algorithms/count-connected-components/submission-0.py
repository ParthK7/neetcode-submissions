class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            if node in visited:
                return 
            
            visited.add(node)
            for child in componentMap[node]:
                dfs(child)

        componentMap = {i:[] for i in range(n)}
        
        for s, d in edges:
            componentMap[s].append(d)
            componentMap[d].append(s)
        
        visited = set()
        compCount = 0

        for node in range(n):
            if node not in visited:
                compCount += 1
                dfs(node)
        
        return compCount
        
