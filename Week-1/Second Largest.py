def find_second_largest(arr):
    # Code Here
    arr1 = sorted(set(arr))
    if len(arr1) < 2:
        return -1
    else:
        return arr1[-2]

# Example usage
# if __name__ == "__main__":
def main():
    n = int(input("Enter the number of elements in the array: "))
    arr = list(map(int, input.split()))
    res = find_second_largest(arr)
    print(res)