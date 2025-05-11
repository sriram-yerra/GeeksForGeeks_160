class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # return arr.sort()
        low = 0         # Pointer for 0s
        mid = 0         # Pointer for 1s
        high = len(arr) - 1  # Pointer for 2s
        
        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]  # Swap 0 to the beginning
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1  # 1 is in the correct position, just move the mid pointer
            else:  # arr[mid] == 2
                arr[high], arr[mid] = arr[mid], arr[high]  # Swap 2 to the end
                high -= 1


