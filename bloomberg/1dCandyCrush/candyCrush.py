# not bad, but you shouldve implemented a seperate class for the character
# should have made a basic stack class, then had the crushStack class inherit from it
class Character(object):
  def __init__(self, val):
    self.val = val
    self.count = 1


class CrushStack():
  def __init__(self):
    self.list = []

  def not_empty(self):
    return len(self.list) > 0

  def peek(self):
    return self.list[-1]

  def pop(self):
    return self.list.pop();

  def push(self, thing):
    self.list.append(thing)
    return self.list

  def match_char(self, character):
    if self.not_empty():
      last = self.peek()
      if character == last["ch"]:
        return True
      else:
        return False
    else:
      return False
  
  def add_to_last(self):
    if self.not_empty():
      last = self.pop()
      self.push({ "ch": last["ch"], "count": last["count"] + 1 })

      


class Solution():
  
  def crush_candy(self, board):
    stack = CrushStack()
    for char in board:
      if stack.not_empty():
        top = stack.peek()
        if stack.match_char(char):
          stack.add_to_last()
        elif top["count"] > 2:
          stack.pop()
          if stack.match_char(char):
            stack.add_to_last()
          else:
            stack.push({ "ch": char, "count": 1 })
        else:
          stack.push({ "ch": char, "count": 1 })
      else:
        stack.push({ "ch": char, "count": 1 })
    if stack.peek()["count"] > 2:
      stack.pop()
    
    return ''.join([char["ch"] * char["count"] for char in stack.list])

sol = Solution()

print(sol.crush_candy('aaabbbc'));

print(sol.crush_candy('aabbbacd'));

print(sol.crush_candy('sssshbbcccbfff'));
