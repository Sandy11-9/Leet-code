class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        nums.reverse()
        k=k%len(nums)
        i=0
        j=k-1
        m=len(nums)-1
        self.rev(i,j,nums)
        self.rev(k,m,nums)


    def rev(self,a,b,nums):
        while(a<b):
            temp=nums[a]
            nums[a]=nums[b]
            nums[b]=temp
            a+=1
            b-=1
        


        