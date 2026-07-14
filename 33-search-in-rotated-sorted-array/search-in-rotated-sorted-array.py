class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s=0
        maxm=max(nums)
        oe=nums.index(maxm)
        os=oe+1
        e=len(nums)+1
        if target in nums[s:oe+1]:
            return nums.index(target)
        elif target in nums[os:e+1]:
            return nums.index(target)
        else:
            return -1
            

        