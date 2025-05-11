#User function Template for python3

class Solution:
    def search(self, pat, txt):
        # code here
        t = txt
        p = pat
        l = []
        m = len(txt)
        n = len(pat)
        for i in range(0,m):
            if t[i] == p[0]:
                if t[i:i+n] == pat:
                    l.append(i)
        return l
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans) == 0:
            print("[]", end="")
        for value in ans:
            print(value, end=' ')
        print()

# } Driver Code Ends