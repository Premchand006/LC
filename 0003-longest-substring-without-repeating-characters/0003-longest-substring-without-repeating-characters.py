class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()       
        left = 0           
        max_length = 0     

        # Loop through each character using the right pointer
        for right in range(len(s)):
            # If character is already in the set, move the left pointer
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            # Add the current character and update max length
            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
