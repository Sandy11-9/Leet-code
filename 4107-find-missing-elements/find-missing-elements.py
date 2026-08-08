class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        li=[]
        for i in range(min(nums),max(nums)+1):
            if i not in nums:
                li.append(i)
        return li
        