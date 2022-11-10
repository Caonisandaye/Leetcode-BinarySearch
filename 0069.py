##LC 69. py file template

#Solution
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l < r:
            m = (l + r + 1) // 2
            if m ** 2 > x:
                r = m - 1
            else:
                l = m
        return l
                
#Result Runtime: 43 ms / 89.58%; Memory Usage: 13.9 MB / 56.62%

#Instruction:
#容易判断是f(i) = i ** 2且属于f类二分查找
