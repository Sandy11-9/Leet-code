class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        l=[]
        if max(nums)<10:
            return nums
        for num in nums:
            m=num%10
            n=num//10
            if n>0:
                l.append(n) 
            if m>0:
                l.append(m)
        return l
        """
        li=[]
        for num in nums:
            s=str(num)
            for st in s:
                li.append(int(st))
        return li




