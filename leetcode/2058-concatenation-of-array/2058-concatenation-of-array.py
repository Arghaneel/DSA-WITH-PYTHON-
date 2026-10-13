class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        n = len(nums)
        array = [0] * (2*n)

        for i in range(n):
            array[i] = nums[i]
            array[i+n] = nums[i]
            
        return array
