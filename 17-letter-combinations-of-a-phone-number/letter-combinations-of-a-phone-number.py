class Solution(object):
    #pl=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        li=[]
        self.comb(0,digits,li,"")
        return li

    def comb(self,i,d,li,ans):
        pl=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]    
        if(i==len(d)):
            li.append(ans)
            return

        idx=int(d[i])
        s=pl[idx]
        for j in range(len(s)):
            self.comb(i+1,d,li,ans+s[j])


