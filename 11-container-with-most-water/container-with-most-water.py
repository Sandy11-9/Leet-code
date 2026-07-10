class Solution(object):
    def maxArea(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        r=len(h)-1
        maxa=0
        while(r>l):
            if(h[l]<h[r]):
                area=h[l]*(r-l)
                l=l+1
            else:
                area=h[r]*(r-l)
                r=r-1
            maxa=max(maxa,area)
        return maxa

        

        