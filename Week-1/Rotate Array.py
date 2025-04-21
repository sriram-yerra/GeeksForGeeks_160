def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k > n
    return arr[-k:] + arr[:-k]

if __name__ == "__main__":
    array = list(map(int, input("Enter the array elements separated by space: ").split()))
    steps = int(input("Enter the number of steps to rotate: "))
    print("Original array:", array)
    print("Rotated array:", rotate_array(array, steps))