from collections import Counter
class Solution:
    def minChar(self, s):
        rev_s = s[::-1]
        concat = s + "#" + rev_s
        lps = [0] * len(concat)

        for i in range(1, len(concat)):
            length = lps[i - 1]
            while length > 0 and concat[i] != concat[length]:
                length = lps[length - 1]
            if concat[i] == concat[length]:
                length += 1
            lps[i] = length

        return len(s) - lps[-1]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        obj = Solution()
        ans = obj.minChar(s)
        print(ans)
        print("~")

# } Driver Code Ends