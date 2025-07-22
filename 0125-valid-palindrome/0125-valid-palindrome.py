class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Keep only letters and numbers, convert to lowercase
        cleaned = ''
        for char in s:
            if char.isalnum():
                cleaned += char.lower()
        
        # Check if cleaned string is the same forwards and backwards
        return cleaned == cleaned[::-1]
