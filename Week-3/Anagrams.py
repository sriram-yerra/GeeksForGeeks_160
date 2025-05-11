from collections import Counter 
class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
       #code here
        # m = len(s2)
        # n = len(s1)
        # if m != n:
        #     return "false"
        # for s in s1:
        #     if s in s2:
        #         s2 = s2.replace(s,"",1)
        #         return "true"
        #     else:
        #         return "false"
        # return "true"
        return Counter(s1) == Counter(s2)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = input().strip()
        b = input().strip()
        if (Solution().areAnagrams(a, b)):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends