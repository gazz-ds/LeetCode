class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
# Instead of for i in range(len(nums)):
        for i in range(len(nums) - 1, 0, -1): # Start at end, move to 0
            if nums[i] == nums[i-1]:
                nums.pop(i)
        