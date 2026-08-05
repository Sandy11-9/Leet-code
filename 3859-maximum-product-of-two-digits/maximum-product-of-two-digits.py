class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        #for i in range():
        li=[]
        while(n!=0):
            a=n%10
            li.append(a)
            n=n//10
        ma=0
        for i in range(len(li)-1):
            for j in range(i+1,len(li)):
                a=li[i]*li[j]
                ma=max(ma,a)
        return ma




        