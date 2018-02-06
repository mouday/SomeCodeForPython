"""
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l_new = cur = ListNode(None)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return l_new.next

def main():
    l11 = ListNode(1)
    l12 = ListNode(2)
    l13 = ListNode(3)
    l11.next = l12
    l12.next = l13
    
    l21 = ListNode(4)
    l22 = ListNode(5)
    l23 = ListNode(6)
    l21.next = l22
    l22.next = l23
    s=Solution()
    l = s.mergeTwoLists(l11, l21)
    print(l)
    # while True:
    #     print(l11.val)
        
    #     if l11.next != None:
    #         l11 = l11.next
    #     else:
    #         break

if __name__ == '__main__':
    main()
