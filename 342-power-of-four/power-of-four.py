class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i=0
        flag=0
        if (n-1)%3==0 and (n & (n-1))==0 and n>0:
            return True
        else:
            return False

        