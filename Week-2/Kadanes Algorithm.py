def kadanes_algorithm(arr):
    max_current = max_global = arr[0]

    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current

    return max_global


if __name__ == "__main__":
    array = list(map(int, input("Enter the array elements separated by spaces: ").split()))
    print("Maximum contiguous subarray sum is:", kadanes_algorithm(array))