class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sArray, tArray = [0] * 26, [0] * 26

        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            sArray[index] += 1

            index = ord(t[i]) - ord('a')
            tArray[index] += 1
        
        return sArray == tArray

        