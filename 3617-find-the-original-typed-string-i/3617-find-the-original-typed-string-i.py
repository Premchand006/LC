class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        if len(word) <= 1:
            return 1
        groups = []
        i = 0
        while i < len(word):
            count = 1
            while i + count < len(word) and word[i] == word[i + count]:
                count += 1
            if count > 1:
                groups.append(count)
            i += count

        if not groups:
            return 1
    
        total = 1 
        for group_size in groups:
            total += group_size - 1
        
        return total