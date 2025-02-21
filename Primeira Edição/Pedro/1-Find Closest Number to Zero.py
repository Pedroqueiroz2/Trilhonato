class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min = nums[0]
        for num in nums:
            if abs(num) < abs(min):
                min = num

        if abs(min) in nums:
            return abs(min)
        else:
            return min
