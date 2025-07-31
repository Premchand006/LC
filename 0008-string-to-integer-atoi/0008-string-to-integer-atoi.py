class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()  # Step 1: Remove leading whitespaces
        if not s:
            return 0
        sign = 1
        result = 0
        index = 0

        # Step 2: Check sign
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1

        # Step 3: Convert digits
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1
        result *= sign

        # Step 4: Clamp result to 32-bit signed int range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result