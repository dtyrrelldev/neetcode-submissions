class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while (top < bottom):
            mid = (top + bottom) // 2
            num = matrix[mid][-1]

            if (num == target): 
                return True
            elif (num < target):
                top = mid + 1
            else:
                bottom = mid
        
        l = 0
        r = len(matrix[top]) - 1

        while (l <= r):
            mid = (l + r) // 2
            num = matrix[top][mid]
            print(matrix[top])
            print(l, r)
            print(num )

            if (num == target):
                return True
            elif (num < target):
                l = mid + 1
            else:
                r = mid - 1

        
        return False
        