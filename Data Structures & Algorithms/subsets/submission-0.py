class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(currArr, currIndex):
            if currIndex == len(nums):
                res.append(currArr.copy())
                return
            
            currArr.append(nums[currIndex])
            backtrack(currArr, currIndex + 1)
            currArr.pop()

            backtrack(currArr, currIndex + 1)
        
        backtrack([], 0)
        return res
        