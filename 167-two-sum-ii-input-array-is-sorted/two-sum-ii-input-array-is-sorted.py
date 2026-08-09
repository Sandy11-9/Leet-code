class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        for i in range(len(numbers)-1):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]
        """
        i=0
        j=len(numbers)-1
        while(True):
            if numbers[i]+numbers[j]==target:
                return [i+1,j+1]
            elif numbers[i]+numbers[j]>target:
                j-=1
            else:
                i+=1