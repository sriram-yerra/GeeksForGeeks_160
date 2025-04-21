def reverse_array(arr):
    # return arr[::-1]
    return reversed(arr)

if __name__ == "__main__":
    array = list(map(int, input("Enter the array elements separated by space: ").split()))
    print("Original Array:", array)
    reversed_array = list(reverse_array(array))  # Convert reversed object to list
    print("Reversed Array:", reversed_array)