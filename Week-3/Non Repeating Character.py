from collections import Counter
class Solution:
    def nonRepeatingChar(self,s):
        #code here
        val = ""
        c = Counter(s)
        for ch in s:
            if c[ch] == 1:
                val += ch
                break
        if val == "":
            return '$'
        return val
    


