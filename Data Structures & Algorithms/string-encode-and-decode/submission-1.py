class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        ans = []

        i = 0 
        
        while i < len(s):
            number = ""

            while s[i] != "#":
                number += s[i]
                i += 1
            length = int(number)
            i += 1

            word = ""
            for index in range(i, i + length):
                word += s[index]
            ans.append(word)

            i = i + length
        return ans
