class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        storedUniqueNums = set(nums)

        for num in nums :
            streak, curr = 0, num
            while curr in storedUniqueNums:
                streak += 1
                curr += 1
            result = max(streak, result)
        return result
        
        
