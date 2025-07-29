class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Convert to string and handle negative sign
        if x < 0:
            reversed_str = str(x)[:0:-1]
            reversed_int = -int(reversed_str)
        else:
            reversed_str = str(x)[::-1]
            reversed_int = int(reversed_str)

        # Check 32-bit signed integer range
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0
            
        return reversed_int