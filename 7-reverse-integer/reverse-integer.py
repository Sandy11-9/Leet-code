class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev=0
        flag=0
        x_max=(2**31)-1
        x_min=-2**31
        if x<0:
            flag=1
            x=-x
        while(x>0):
            if rev>x_max/10 or rev<x_min/10:
                return 0
            d=x%10
            rev=(rev*10)+d
            x=x//10
        if flag==1:
            r=-rev
            return r
        return rev
        