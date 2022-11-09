##LC 0. py file template

#Solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = len(nums)
        pivot = 0
        if nums[0] > nums[-1]:
            l, r = 0, L - 1
            while l < r:
                m = (l + r + 1) // 2
                if nums[m] < nums[m - 1]:
                    pivot = m
                    break
                elif nums[m] > nums[0]:
                    l = m
                else:
                    r = m - 1
            else:
                pivot = l
            print(pivot)
        l, r = 0, L - 1
        while l <= r:
            m = (l + r) // 2
            idx = (m + pivot) % L
            if nums[idx] == target:
                return idx
            elif nums[idx] < target:
                l = m + 1
            else:
                r = m - 1
        return - 1
                
#Result Runtime: 67 ms / 74.17%; Memory Usage: 14.2 MB / 56.13%

#Instruction: XXXXXX
