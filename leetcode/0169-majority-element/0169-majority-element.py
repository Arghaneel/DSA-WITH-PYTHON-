class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq = {}
        n = len(nums)/2
        for i in nums:
            if i in freq:
                freq[i] +=1
            else:
                freq[i] = 1
        
        for i in nums:
            if freq[i] > n:
                return i
                break