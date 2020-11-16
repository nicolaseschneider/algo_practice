class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
  def reverseBetween(self, head, m, n):
    dummy = ListNode(0, head)
    pre = dummy
    for i in range(0,m - 1):
      pre = pre.next
    
    
    curr = pre.next

    for i in range(0, n-m):
      _next = curr.next
      curr.next = _next.next
      _next.next = pre.next
      pre.next = _next
      
    return dummy.next
      