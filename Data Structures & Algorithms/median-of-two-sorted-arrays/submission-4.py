from bisect import bisect_left, bisect_right
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        half = (len(nums1) + len(nums2)) // 2
        l = -(10 ** 6) - 1
        r = 10 ** 6 + 1
        while r - l  > 1:
            m = (l + r) // 2
            less = bisect_left(nums1, m) + bisect_left(nums2, m)
            if less <= half:
                l = m
            else:
                r = m
        l1 = -(10 ** 6) - 1
        r1 = 10 ** 6 + 1
        while r1 - l1  > 1:
            m = (l1 + r1) // 2
            more = len(nums1) + len(nums2) - bisect_right(nums1, m) - bisect_right(nums2, m)
            if more <= half:
                r1 = m
            else:
                l1 = m
        return (l + r1) / 2