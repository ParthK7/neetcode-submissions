class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for child in newGraph[node]:
                if child in visited:
                    if child != parent:
                        return False
                    else:
                        continue
                
                if not dfs(child, node):
                    return False
            return True 

        visited = set()

        newGraph = { i : [] for i in range(n)}

        for s, d in edges:
            newGraph[s].append(d)
            newGraph[d].append(s)

        if not dfs(0, -1):
            return False
        return len(visited) == n