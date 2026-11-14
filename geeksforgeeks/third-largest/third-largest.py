class Solution:
    def thirdLargest(self, arr):
        if len(arr) < 3:
            return -1
        arr.sort(reverse=True)  # Sorts in-place without removing duplicat
        return arr[2]