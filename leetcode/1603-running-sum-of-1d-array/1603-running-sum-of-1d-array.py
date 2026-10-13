class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n = len(nums)
        array = [0] * (1* n)
        sum = 0 

        for i in range(n):
            sum =sum + nums[i]
            array[i] = sum
            
        return array