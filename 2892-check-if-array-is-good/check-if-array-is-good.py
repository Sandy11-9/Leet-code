class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        flag=0
        for i in range(1,len(nums)-1):
            if i not in nums:
                flag=1
                break
        maxim=max(nums)
        if len(nums)==maxim+1 and flag==0 and nums.count(maxim)==2:
            return True
        else:
            return False
        