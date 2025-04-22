class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        if n == 1:
            return 0

        # Sort the array
        arr.sort()

        # Initial difference
        diff = arr[-1] - arr[0]

        for i in range(1, n):
            if arr[i] - k < 0:
                continue

            max_height = max(arr[i-1] + k, arr[-1] - k)
            min_height = min(arr[0] + k, arr[i] - k)

            diff = min(diff, max_height - min_height)

        return diff
