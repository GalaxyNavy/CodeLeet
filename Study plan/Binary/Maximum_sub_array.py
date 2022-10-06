#Trace line by line 


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        temp = 0
        HighSum = nums[0]
        
        

        for i in nums :
            temp = temp + i
            
            #You need toevaluate both the cases or condition for passing all test cases!,, 
        
            if temp > HighSum  : 
            
                HighSum = temp
                
                
            if temp < 0:            
                temp = 0

        


        return HighSum
        


        
