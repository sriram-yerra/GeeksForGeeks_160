def next_permutation(nums):
    n = len(nums)
    i = n - 2

    # Find the first decreasing element
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        # Find the next larger element to swap with
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    # Reverse the elements after the swapped index
    nums[i + 1:] = reversed(nums[i + 1:])

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Original:", nums)
    next_permutation(nums)
    print("Next Permutation:", nums)