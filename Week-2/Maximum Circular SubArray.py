def max_circular_subarray(arr):
    def kadane(nums):
        max_current = max_global = nums[0]
        for num in nums[1:]:
            max_current = max(num, max_current + num)
            max_global = max(max_global, max_current)
        return max_global

    total_sum = sum(arr)
    max_kadane = kadane(arr)
    max_wrap = total_sum + kadane([-x for x in arr])

    if max_wrap == 0:
        return max_kadane
    return max(max_kadane, max_wrap)


if __name__ == "__main__":
    arr = list(map(int, input("Enter the array elements separated by space: ").split()))
    result = max_circular_subarray(arr)
    print("Maximum Circular Subarray Sum:", result)