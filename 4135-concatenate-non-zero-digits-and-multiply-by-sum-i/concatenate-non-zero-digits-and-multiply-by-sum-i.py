class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        li=[]
        sum1=0
        if n==0:return 0
        while(n>0):
            x=n%10
            n=n//10
            if(x != 0):
                li.append(x)
                sum1=sum1+x
        li.reverse()
        num= int("".join(map(str, li)))
        ans=num*sum1
        return ans

        