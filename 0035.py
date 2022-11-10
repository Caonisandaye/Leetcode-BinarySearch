
##LC 35. py file template

#Solution
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1] < target:
            return len(nums)
        
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l

#Result Runtime: 60 ms / 83.23%; Memory Usage: 14.7 MB / 82.28%

#Instruction:
#好像也没什么好讲的，f(i)和二分查找的种类很好判断。哦简单题，那没事了。
