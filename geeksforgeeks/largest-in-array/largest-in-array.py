class Solution:
    def largest(self, arr):
        # code here
        largest = arr[0]
        for num in range(1,len(arr)):
            if largest < arr[num]:
                largest = arr[num]
            
        return largest 
