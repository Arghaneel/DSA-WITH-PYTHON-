class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        remaining = nums[:-k]
        rotated = nums[-k:]
        nums[:] = rotated + remaining