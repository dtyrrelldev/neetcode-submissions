class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while (stack and stack[-1][1] > h):
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            
            stack.append((start, h)) # we append the index(start) of the popped bar  here because we know that 
            # the previous bar will be higher , so we can use the start of the previous bar's index 
            # as the left boundary of the new bar

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        
        return max_area
