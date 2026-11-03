class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        cols = len(matrix[0])
        rows = len(matrix)
        l = 0
        r = rows*cols - 1

        while l <= r :
            mid = (r+l)//2

            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False