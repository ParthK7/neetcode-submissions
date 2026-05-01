class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def visitCell(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == -1:
                return 
            
            visited.add((r, c))
            queue.append((r, c))

        queue = deque([])
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
        
        steps = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = steps

                visitCell(r + 1, c)
                visitCell(r - 1, c)
                visitCell(r, c + 1)
                visitCell(r, c - 1)
            
            steps += 1
        
        print(grid)

