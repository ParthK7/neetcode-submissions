class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(word, currIndex, r, c, visited):
            if currIndex >= len(word):
                return True
            
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or board[r][c] != word[currIndex]:
                return False
            
            visited.add((r, c))
            return (dfs(word, currIndex + 1, r + 1, c, visited) or 
                    dfs(word, currIndex + 1, r - 1, c, visited) or 
                    dfs(word, currIndex + 1, r, c + 1, visited) or 
                    dfs(word, currIndex + 1, r, c - 1, visited))

        res = []
        ROWS, COLS = len(board), len(board[0])
        for word in words:
            for r in range(ROWS):
                for c in range(COLS):
                    if dfs(word, 0, r, c, set()):
                        res.append(word)
        return res
                
        
        
        
            