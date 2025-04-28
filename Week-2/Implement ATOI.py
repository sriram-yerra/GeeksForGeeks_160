class Solution:
    def myAtoi(self, s):
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1

        if i < len(s) and s[i] == '-':
            sign = -1
            i += 1
        elif i < len(s) and s[i] == '+':
            sign = 1
            i += 1
        else:
            sign = 1  # default to positive if no sign

        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX
        else:
            return result

