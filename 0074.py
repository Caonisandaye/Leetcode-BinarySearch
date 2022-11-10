##LC 74. py file template

#Solution
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrow, ncol = len(matrix), len(matrix[0])
        
        l, r = 0, nrow * ncol - 1
        while l <= r:
            m = (l + r) // 2
            row, col = m // ncol, m % ncol
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = m + 1
            else:
                r = m - 1
        return False
                
#Result Runtime: 37 ms / 99.50%; Memory Usage: 14.3 MB / 89.58%

#Instruction:
#关键点在于如何把某个数在整个矩阵中的排序（从0开始计数）和行／列坐标互相转化。做到这一点后很容易判断f(i) = matrix[i//col][i%col]且属于a类二分查找（target）不一定存在
