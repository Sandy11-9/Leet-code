class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    count+=1
                    self.mzero(grid,i,j)
        return count

    def mzero(self,grid,r,c):
        if r>=len(grid) or c>=len(grid[0]) or r<0 or c<0 or grid[r][c]=='0':
            return
        grid[r][c]='0'
        self.mzero(grid,r,c+1)
        self.mzero(grid,r,c-1)
        self.mzero(grid,r+1,c)
        self.mzero(grid,r-1,c)


        