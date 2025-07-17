class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Just combine both arrays and sort them
        all_numbers = nums1 + nums2
        all_numbers.sort()
        
        # Find the middle
        total_count = len(all_numbers)
        middle = total_count // 2
        
        # If we have odd number of elements, return the middle one
        if total_count % 2 == 1:
            return float(all_numbers[middle])
        
        return (all_numbers[middle - 1] + all_numbers[middle]) / 2.0