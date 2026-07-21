class Solution(object):
    def searchMatrix(self, mat, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        
        n=len(mat[0])
        m=len(mat)
        s=0
        e=(m*n)-1

        while(s<=e):
            mid =(s+e)//2
            row=mid//n
            col=mid%n 
            if mat[row][col]==target:
                return True
            elif mat[row][col]<target:
                s=mid+1
            else:
                e=mid-1
        return False
        """
        for r in mat:
            if target in r:
                return True
        return False