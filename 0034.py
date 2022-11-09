##LC 0034. py file template

#Solution
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        if nums and nums[l] == target:
            first = l
        else:
            return [-1, -1]
        
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r + 1) // 2
            if nums[m] > target:
                r = m - 1
            else:
                l = m
        last = l
        
        return [first, last]
                
#Result Runtime: 130 ms / 75.71%; Memory Usage: 15.5 MB / 10.40%

#Instruction: 
#两次二分查找，f(i)和类型都非常好判断。LC不会是按照二分查找的次数来判断题目难度的吧，好迷。
