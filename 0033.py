##LC 0033. py file template

#Solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = len(nums)
        pivot = 0
        if nums[0] > nums[-1]:
            l, r = 0, L - 1
            while l < r:
                m = (l + r) // 2
                if m > 0 and nums[m] < nums[m - 1]:
                    pivot = m
                    break
                elif nums[m] >= nums[0]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                pivot = l
                
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

#Instruction:
#非典型二分法题目，大体思路是做两次二分查找。
#第一次找到pivot，使得整个列表往左移动pivot个单位（左边溢出的元素填补到右边去）之后，整个列表单调递增。换句话说就是num[(i+pivot)%L]是单调递增的。
#注意这一次查找的f(i)很难用显示函数表达，但是当前检查的index过大和过小很容易判断。
#剔除了pivot = 0的情况后（我想不出把包括0的情况写一起怎么处理比较简洁），本次二分查找属于a类型，且答案必定存在。
#为了和我们的cheatsheet保持基本一致，我把这里的+1/-1处理的比较繁琐，如果追求代码简洁的话可以想想怎么改。
#第二次就很自然的对[0, L-1]上的index进行二分查找，f(i) = num[(i+pivot)%L]，target已给出。本次二分查找属于a类型，且答案可能不存在。
