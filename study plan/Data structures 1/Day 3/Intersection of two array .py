class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """



         #Use print statement to trace the code

        c = Counter(nums1)
        r = []
        
        for n in nums2:
           
            if c[n] > 0:
                
                r.append(n)
                c[n] = c[n]-1
        
        return r
