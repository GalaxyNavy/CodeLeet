class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        hashset = set()

        
        for item in nums:
            if item in hashset:
                return True
            hashset.add(item)

    

        return False
    
    
    
#  Another best solution:
  class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        hashset = set(nums)
        


        
        if len(hashset) < len(nums):
            return True


        return False
