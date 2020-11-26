class Solution(object):
    def addTwoNumbers(self, l1, l2, carry = 0):
      
      if l1 is None and l2 is None and carry == 0:
        return None
  
      l1val = 0 if l1 is None else l1.val
      l2val = 0 if l2 is None else l2.val

      sum = l1val + l2val + carry
      digit = sum % 10
      
      if sum > 9:
        carry = 1
      else:
        carry = 0
      
      l1Next = None if l1 is None else l1.next
      l2Next = None if l2 is None else l2.next
      
      
      newNode = ListNode(digit)
      newNode.next = self.addTwoNumbers(l1Next, l2Next, carry)
      return newNode