class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        sum_o=0
        sum_e=0
        for i in range(1,n*2+1):
            if i%2==0:
                sum_e=sum_e+i
            else:
                sum_o=sum_o+i
        while(sum_e!=0):
            #sum_o,sum_e= sum_e, sum_o % sum_e
            temp=sum_e
            sum_e=sum_o % sum_e
            sum_o=temp
        return sum_o
        """
        return n
        