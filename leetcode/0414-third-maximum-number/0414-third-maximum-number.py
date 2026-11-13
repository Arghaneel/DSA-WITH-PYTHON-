class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        num = sorted(set(nums), reverse = True)
        if len(num) >= 3:
            return num[2]
        else:
            return num[0]