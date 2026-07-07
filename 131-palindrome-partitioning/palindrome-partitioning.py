class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        li=[]
        ans=[]
        self.pp(s,li,ans)
        return li
    
    def pp(self,s,li,ans):

        if(len(s)==0):
            li.append(ans[:]) 
            return
        for i in range(len(s)) :
            if(self.ispal(s[0:i+1])):
                ans.append(s[0:i+1])
                self.pp(s[i+1:],li,ans)
                ans.pop(len(ans)-1)
    def ispal(self,s):
        i=0
        j=len(s)-1
        while(i<j):
            if(s[i]!=s[j]):
                return False
            i+=1
            j-=1
        return True
                  