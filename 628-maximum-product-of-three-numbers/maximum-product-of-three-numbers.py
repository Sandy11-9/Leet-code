class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        c=0
        for n in nums:
            if n<0:
                nums.append(-n)
                c+=1
        nums.sort()
        l=len(nums)-1
        if c==1 or c==3:
            return -(nums[l]*nums[l-1]*nums[l-2])
        else:
            return nums[l]*nums[l-1]*nums[l-2]
        """
        nums.sort()
        return max(
            nums[-1]*nums[-2]*nums[-3],nums[1]*nums[0]*nums[-1]
        )
        