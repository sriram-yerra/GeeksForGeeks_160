def move_zeros_to_end(arr):
    non_zero_index = 0  # Index to place the next non-zero element

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
            non_zero_index += 1

    return arr

if __name__ == "__main__":
    arr = list(map(int, input("Enter the array elements separated by space: ").split()))
    print("Original array:", arr)
    result = move_zeros_to_end(arr)
    print("Array after moving zeros to the end:", result)