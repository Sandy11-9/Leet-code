class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while(True):
            m,num=1,n
            while num!=0:
                a=num%10
                m*=a
                num=num//10
            if m%t == 0:
                return n  
            n+=1
            
        