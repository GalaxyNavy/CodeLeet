
# Trace Line by line



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
      
            if temp > HighSum  :
               
                HighSum = temp
              
            if temp < 0:              
                
                temp = 0

        


        return HighSum
        


        
