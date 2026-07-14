class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s=0
        maxm=max(nums)
        oge=nums.index(maxm)
        ogs=oge+1
        e=len(nums)+1
        if target in nums[s:oge+1]:
            return nums.index(target)
        elif target in nums[ogs:e+1]:
            return nums.index(target)
        else:
            return -1
            

        