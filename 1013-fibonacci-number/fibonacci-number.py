class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n==0):
            return 0
        if(n==1):
            return 1
        pre=self.fib(n-1)
        npre=self.fib(n-2)
        return pre+npre
        