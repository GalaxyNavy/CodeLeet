import numpy
class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """


        


        l = []
        new = []

        m = len(mat)
        n = len(mat[0])


        if m*n != r*c :
            return mat

        for i in range(m):
            for j in range(n):
                l.append(mat[i][j])

        
        new = [[ 0 for _ in range(c)] for _ in range(r) ] #must 
#         print(new)

        index = 0
        for i in range(r):
            # new.append([])
            # # print(new)

            for  j in range(c) :
                new[i][j]  = l[index]
                     
                index = index+1


        return (new)
