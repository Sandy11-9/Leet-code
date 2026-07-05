class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        minp=1
        maxp=0
        flag=0

        for i in range(len(prices)):
            if i == len(prices)-1:
                return 0

            if prices[i]==minp:
                flag=1
                for j in range(1,(len(prices)-i)):
                    n=prices[j]-minp
                    maxp=max(n,maxp)
            if(flag==1):
                break
        return maxp 
        """

        minp=prices[0]
        maxp=0
        for i in range(1,len(prices)):
            if prices[i]<minp:
                minp=prices[i]
            else:
                pro=prices[i]-minp
                maxp=max(pro,maxp)
        return maxp
                
        