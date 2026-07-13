class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        num="123456789"
        li=[]
        for j in range(2,10):
            for k in range(0,len(num)-j+1):
                n=int(num[k:k+j])
                if(low<=n and n<=high):
                    li.append(n)
        return li
        
        