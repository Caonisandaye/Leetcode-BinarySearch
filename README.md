# Leetcode-BinarySearch
-- 当我们要用二分查找算法解决问题的时候，我们首先要思考以下前提是否成立 --

<!-- 1.对于我们要寻找的答案i，是否存在包含i的上下界[l,r]和单调递增的函数f(i)和我们希望f(i)等于或者接近的值target
1a.注意对于1，有时候我们并不能保证target落在f(l)和f(r)之间，此时我们需要先检查f(l)和f(r)和target的大小关系，
然后根据题目需要判断l/r是否是我们需要的答案或是答案不存在

2.如果我们能保证i落在[l,r]之中（即l<=i<=r，或者说f(l)<=target<=f(r))，我们需要根据题意判断我们需要找到的i和target的关系是：
2a. 唯一的i， s.t. f(i) == target
2b. 最小的i， s.t. f(i) == target（可能不存在）
2c. 最小的i， s.t. f(i) >= target
2d. 最小的i， s.t. f(i) > target（可能不存在）
2e. 最大的i， s.t. f(i) == target（可能不存在）
2f. 最大的i， s.t. f(i) <= target
2g. 最大的i， s.t. f(i) < target（可能不存在）
 -->
3.对于2的sample code：

3a. 
l, r = l0, r0
while l <= r:
    m = (l + r)/2
    if f(m) == target:
        return m
    elif f(m) > target:
        r = m - 1
    else:
        l = m + 1
return -1

3b. 
l, r = l0, r0
while l < r:
    m = (l + r)/2
    if f(m) >= target:
        r = m
    else:
        l = m + 1
return l if f(l) == target else -1

<!-- 3c. 
l, r = l0, r0
while l < r:
    m = (l + r)/2
    if f(m) >= target:
        r = m
    else:
        l = m + 1
return l if f(l) >= target -->

<!-- 3d.
l, r = l0, r0
while l < r:
    m = (l + r)/2
    if f(m) >= target:
        r = m
    else:
        l = m + 1
return l if f(l) > target else -1 -->

3e.
l, r = l0, r0
while l < r:
    m = l + (r-l+1)/2
    if f(m) > target:
        r = m - 1
    else:
        l = m 
return l if f(l) == target else -1

<!-- 3f. 
l, r = l0, r0
while l < r:
    m = l + (r-l+1)/2
    if f(m) > target:
        r = m - 1
    else:
        l = m 
return l if f(l) <= target -->

<!-- 3g.
l, r = l0, r0
while l < r:
    m = l + (r-l+1)/2
    if f(m) > target:
        r = m - 1
    else:
        l = m
return l if f(l) < target else -1 -->
