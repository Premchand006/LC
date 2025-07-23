class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        for char in columnTitle:
            # Convert letter to number: A=1, B=2, ..., Z=26
            value = ord(char) - ord('A') + 1
            result = result * 26 + value
        return result
