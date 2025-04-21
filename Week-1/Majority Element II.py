from collections import Counter

def majority_element(nums):
    n = len(nums)
    threshold = n // 3
    freq = Counter(nums)
    result = [key for key, count in freq.items() if count > threshold]
    return result

if __name__ == "__main__":
    nums = list(map(int, input("Enter the numbers separated by space: ").split()))
    print("Majority elements are:", majority_element(nums))