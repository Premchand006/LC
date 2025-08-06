class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for i in range(32):          # 32 bits total
            bit = n & 1              # Extract the last bit
            result = (result << 1) | bit  # Shift result left and add the bit
            n >>= 1                  # Shift input right to process next bit
        return result
