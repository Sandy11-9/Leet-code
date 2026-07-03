class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        li=[]
        ans=[]
        self.find(li,ans,nums)
        return li

    def find(self,li,ans,nums):
        if(len(ans)==len(nums)):
            li.append(list(ans))
            return



        for i in range(len(nums)):
            if nums[i] not in ans:
                ans.append(nums[i])
                self.find(li,ans,nums)
                ans.pop(len(ans)-1)
        