class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=min(nums)
        n=max(nums)
        while(n>0):
            temp=n
            n=m%n
            m=temp
        return m

        