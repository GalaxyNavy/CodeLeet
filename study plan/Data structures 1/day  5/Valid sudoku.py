class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

         # creating hash set for rows, cols and box

        rows = collections.defaultdict(set)
        cols =  collections.defaultdict(set)
        squares =  collections.defaultdict(set)



        for r in range(9)  :
            for c in range(9)  :

                if board[r][c] == '.':
                    continue

                if(  (board[r][c] in rows[r]) or
                    (board[r][c] in rows[r]) or 
                    (board[r][c] in squares[ (r//3, c//3) ])    ) :
                
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,  c//3)].add(board[r][c])



        return True




        
