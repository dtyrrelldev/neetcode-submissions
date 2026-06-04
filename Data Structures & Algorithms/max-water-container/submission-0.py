class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current_len = len(heights) - 1
        max_area = 0

        l = 0
        r = len(heights) - 1

        while (l < r):
            max_ht_idx = -1
            if (heights[l] < heights[r]):
                min_ht_idx = l
                l += 1
            else:
                min_ht_idx = r
                r -= 1

            area = heights[min_ht_idx] * current_len
            max_area = max(max_area, area)
            current_len -= 1
        
        return max_area
        