class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        e=len(nums1)
        if e%2==0:
            return (nums1[(e//2)-1] + nums1[e//2])/2.0
        else:
            return nums1[e//2]
            