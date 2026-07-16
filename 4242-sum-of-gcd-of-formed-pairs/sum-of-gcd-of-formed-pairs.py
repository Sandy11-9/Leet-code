class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def gcd(a,b):
            while(b>0):
                a,b=b,a%b
            return a

        m=[]
        pre=[]
        m.append(nums[0])
        pre.append(gcd(nums[0],m[0]))
        for i in range(1,len(nums)):
            #maa=max(nums[i-1],nums[i])
            maa=max(m[i-1],nums[i])
            m.append(maa)
            #a=gcd(nums[i-1],m[i-1])
            a=gcd(maa,nums[i])
            pre.append(a)
        #pre.append(gcd(nums[len(nums)-1],m[len(m)-1]))
        pre.sort()
        i=0
        j=len(pre)-1
        sum=0

        while(i<j):
            sum+=gcd(pre[i],pre[j])
            i+=1
            j-=1
        
        return sum
        """
        if(len(pre)%2==0):
            
            while(pre):
                a=min(pre)
                b=max(pre)
                gc=gcd(a,b)
                sum+=gc
                pre.remove(a)
                pre.remove(b)
            
            for i in range(len(pre)//2):
                sum=sum+pre[i]
        else:
            while(len(pre)!=1):
                a=min(pre)
                b=max(pre)
                gc=gcd(a,b)
                sum+=gc
                pre.remove(a)
                pre.remove(b)
            for i in range(len(pre)//2):
                sum=sum+pre[i]
        

        return sum
        """
        