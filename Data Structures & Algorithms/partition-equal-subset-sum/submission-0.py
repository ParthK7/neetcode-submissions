class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False
        
        target = total / 2

        def backtrack(currIndex, currSum):
            if currSum == target:
                return True
            
            if currIndex >= len(nums) or currSum > target:
                return False

            if backtrack(currIndex + 1, currSum + nums[currIndex]): return True
            if backtrack(currIndex + 1, currSum): return True
            return False

        return backtrack(0, 0)