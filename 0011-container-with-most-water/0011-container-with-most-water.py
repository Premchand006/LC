class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        max_area=0

        while left<right:
            # Calculate the area formed by the lines at left and right
            width=right-left
            min_height=min(height[left], height[right])
            area=width*min_height
            max_area=max(max_area, area)

            # Move the pointer pointing to the shorter line inward
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area