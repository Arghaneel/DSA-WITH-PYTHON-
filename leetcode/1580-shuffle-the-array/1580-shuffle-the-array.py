class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        array = [0] * (2 * n )

        for i in range(n):
            array[2 * i] = nums[i]
            array[2 * i + 1] = nums[i + n]
        
        return array