class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left=0
        right=x-1
        if x==0:
            return 0
        elif x==1:
            return 1
        while(left<=right):
            mid=(right+left)//2
            if int(mid*mid)==x:
                return mid
            elif mid*mid<x:
                left=mid+1
            else:
                right=mid-1
        return left-1

        
            


        