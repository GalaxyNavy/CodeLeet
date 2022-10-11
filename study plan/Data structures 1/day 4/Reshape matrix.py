class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
      


        store = [[1], [1,1] ]


        if numRows == 0 :
            store =   []
            return store



        if numRows == 1 :
            store = [[1]]
            return store 
          
        if numRows == 2 :
            
            store =  [[1], [1,1]] 
            return store

        for i in range(1,numRows-1 ) :
            temp = []
            temp.append(1)
            
            for j in range( len(store[i] )  - 1  )   :  
                adding = store[-1][j] +  store[-1][j+1]  
                temp.append(adding)
                
            temp.append(1)
         
            store.append(temp)
            
            #print(store)
      
        return store






