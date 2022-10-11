

import numpy

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """



        arr = numpy.array(matrix)
        
#         this can have O(n) 
        for i in numpy.nditer(arr) :
            if target == i: 
                return True

        
        
        
        #this can run in o(n*n) 
        # for  i in matrix:
        #     for j in i :
        #         if j == target :
        #             return True

        

        return False
