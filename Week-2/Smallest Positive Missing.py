def find_smallest_missing_positive(arr):
    # Filter positive numbers and remove duplicates
    arr = set(filter(lambda x: x > 0, arr))
    smallest = 1

    # Find the smallest missing positive integer
    while smallest in arr:
        smallest += 1

    return smallest

if __name__ == "__main__":
    # Input from user
    try:
        user_input = input("Enter a list of integers separated by spaces: ")
        arr = list(map(int, user_input.split()))
        result = find_smallest_missing_positive(arr)
        print(f"The smallest positive missing number is: {result}")
    except ValueError:
        print("Invalid input. Please enter integers only.")