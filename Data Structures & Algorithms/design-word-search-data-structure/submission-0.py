class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def dfs(self, word, node, currIndex):
        if currIndex >= len(word):
            return node.end
        
        if word[currIndex] in node.children:
            return self.dfs(word, node.children[word[currIndex]], currIndex + 1)
        
        elif word[currIndex] == ".":
            for child in node.children:
                if self.dfs(word, node.children[child], currIndex + 1): return True
            return False
        
        else:
            return False


    def addWord(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root

        a = self.dfs(word, curr, 0)
        return a



        
            
        
