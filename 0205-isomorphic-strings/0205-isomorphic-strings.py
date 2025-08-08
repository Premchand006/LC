class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in range(len(s)):
            if s.index(s[i]) != t.index(t[i]):
                return False
        return True
        