class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """  




        minimum = prices[0]

        maxamount =0

        for i in prices:

            
            if i < minimum :
                minimum = i
                # print(minimum)

            sell = i-minimum
            # print(sell)

            if sell > maxamount  :
                maxamount = sell 
            # maxamount = minimum - 

        return maxamount
