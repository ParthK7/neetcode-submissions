class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        memo = {}

        if total % 2:
            return False
        
        target = total / 2

        def backtrack(currIndex, currSum):
            if (currSum, currIndex) in memo:
                return memo[(currSum, currIndex)]

            if currSum == target:
                return True
            
            if currIndex >= len(nums) or currSum > target:
                return False

            if backtrack(currIndex + 1, currSum + nums[currIndex]) or backtrack(currIndex + 1, currSum):
                memo[(currSum, currIndex)] = True
                return True

            memo[(currSum, currIndex)] = False
            return False

        return backtrack(0, 0)