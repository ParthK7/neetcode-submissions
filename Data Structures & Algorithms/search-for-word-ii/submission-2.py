class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(word, r, c, index, visited):
            if index >= len(word):
                return True
            
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[index] or (r, c) in visited:
                return False
            
            visited.add((r, c))
            return (dfs(word, r + 1, c, index + 1, visited) or 
            dfs(word, r - 1, c, index + 1, visited) or 
            dfs(word, r, c + 1, index + 1, visited) or
            dfs(word, r, c - 1, index + 1, visited))

        res = []
        ROWS, COLS = len(board), len(board[0])

        def word_exists(word):
            for r in range(ROWS):
                for c in range(COLS):
                    if dfs(word, r, c, 0, set()):
                        return True
            return False
            

        for word in words:
            if word_exists(word):
                res.append(word)
        return res