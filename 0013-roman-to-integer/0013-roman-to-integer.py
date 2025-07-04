class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Map Roman numerals to their values
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Process from right to left
        for char in reversed(s):
            value = roman_map[char]
            
            # If current value is less than previous, subtract it
            if value < prev_value:
                total -= value
            else:
                total += value
            
            prev_value = value
        
        return total

# Test cases
solution = Solution()
print(solution.romanToInt("III"))      # Output: 3
print(solution.romanToInt("LVIII"))    # Output: 58
print(solution.romanToInt("MCMXCIV"))  # Output: 1994
print(solution.romanToInt("IV"))       # Output: 4
print(solution.romanToInt("IX"))       # Output: 9
print(solution.romanToInt("XL"))       # Output: 40
print(solution.romanToInt("XC"))       # Output: 90
print(solution.romanToInt("CD"))       # Output: 400
print(solution.romanToInt("CM"))       # Output: 900