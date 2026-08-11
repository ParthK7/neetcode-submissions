class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        numToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        ans = []

        def dfs(currIndex, currWord):
            if currIndex == len(digits):
                ans.append(currWord)
                return 
            
            for char in numToChar[digits[currIndex]]:
                currWord += char
                dfs(currIndex + 1, currWord)
                currWord = currWord[:-1]
        
        dfs(0, "")
        return ans
