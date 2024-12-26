class Solution:
    def validMountainArray(self, arr):
        # ToDo: Write Your Code Here.
        if not arr:
            return False

        index = 0
        while index + 1 < len(arr) and arr[index] < arr[index + 1]:
            index += 1

        if index == 0 or index == len(arr) - 1:
            return False
        
        while index + 1 < len(arr) and arr[index] > arr[index + 1]:
            index += 1

        if index != len(arr) - 1:
            return False

        return True

