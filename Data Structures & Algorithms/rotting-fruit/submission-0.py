class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def rotCells(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or ((r, c)) in visited or grid[r][c] == 0:
                return 
            
            counter[0] -= 1
            queue.append([r, c])
            visited.add((r, c))

        counter = [0, 0]
        queue = deque()
        visited = set()

        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    counter[0] += 1
                elif grid[r][c] == 2:
                    counter[1] += 1
                    queue.append([r, c])
                    visited.add((r, c))
        
        if counter[0] == 0: return 0
        if counter[1] == 0: return -1

        time = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                rotCells(r + 1, c)
                rotCells(r - 1, c)
                rotCells(r, c + 1)
                rotCells(r, c - 1)
            time += 1
        
        if counter[0] == 0:
            return time - 1
        else:
            return -1

