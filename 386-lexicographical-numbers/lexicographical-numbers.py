class Solution(object):

    def lexi(self,num,n,ans):
        if num>n:
            return
        ans.append(num)
        num=num*10
        if num>n:
            return
        for i in range(0,10):
            self.lexi(num+i,n,ans)
    
    def lexicalOrder(self,n):

        ans=[]
        for i in range(1,10):
            self.lexi(i,n,ans)
        return ans
        



