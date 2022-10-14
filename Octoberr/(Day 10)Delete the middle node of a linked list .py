# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """



        pointer =  head
        length = 0
        while pointer:

            
            pointer =  pointer.next

            length =  length+1

      

        if length == 1:
            return head.next

        middle = int(length/2)
=
        temp = head
        head_t= temp
        count = 0

        for node in range(middle) :
            if count == middle-1:
                print(count)
                temp.next = temp.next.next
                # break

            else:
                temp = temp.next

            count = count+1

            

        return head











