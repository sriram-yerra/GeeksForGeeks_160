# User function Template for Python3
class Solution:
    def addBinary(self, s1, s2):
        """
        Function to add two binary strings and return their sum as a binary string.
        """
        # Convert binary strings to integers, add them, and convert the result back to binary
        res = int(s1, 2) + int(s2, 2)
        return bin(res)[2:]  # Remove '0b' prefix from the binary representation

# Driver Code Starts
if __name__ == '__main__':
    T = int(input("Enter the number of test cases: "))
    for _ in range(T):
        a = input("Enter the first binary string: ").strip()
        b = input("Enter the second binary string: ").strip()
        ob = Solution()
        answer = ob.addBinary(a, b)
        print("Sum of binary strings:", answer)
        print("~")
# Driver Code Ends
