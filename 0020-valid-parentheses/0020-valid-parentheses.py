class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                # It's a closing bracket
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                # It's an opening bracket
                stack.append(char)
        
        return len(stack) == 0