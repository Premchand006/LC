class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Edge case: if needle is an empty string, return 0
        if not needle:
            return 0

        # Loop through haystack and check substrings
        for i in range(len(haystack) - len(needle) + 1):
            # Check if the substring from i to i+len(needle) matches needle
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
