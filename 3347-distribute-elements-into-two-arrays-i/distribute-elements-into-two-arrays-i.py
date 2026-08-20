class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        arr1=[]
        arr2=[]
        for i in range(0,len(nums)):
            if i==len(nums)-1:
                if arr1[-1]<arr2[-1]:
                    arr2.append(nums[i])
                else:
                    arr1.append(nums[i]) 
            elif i%2==0:
                arr1.append(nums[i])
            elif i%2!=0:
                arr2.append(nums[i])
        return arr1+arr2
        """
        arr1=[nums[0]]
        arr2=[nums[1]]
        for i in range(2,len(nums)):
            if arr1[-1]<arr2[-1]:
                arr2.append(nums[i])
            else:
                arr1.append(nums[i])
        return arr1+arr2