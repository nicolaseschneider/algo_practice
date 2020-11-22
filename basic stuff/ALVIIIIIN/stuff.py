# 

# Graph? 
# collection of nodes and edges

# Tree?
# 

#   a
#  /   \ 
# b -> c 

# (a,b)
# (a,c)
# (b,c)

#       10
#     /    \
#    5     15
#   / \
#  3   6   
#       \
#        17

#     a
#    / \
#   b   c
#  / \   \
# d   e   f


# breadthFirst - a, b, c, d, e, f 
# depthFirst -  a, b, d, e, c, f


# Given the root of a b. tree. Write a fn that prints all nodes of the 
# tree in breadth first order.



class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


#     a
#    / \         
#   b   c      
#  / \   \        #       
# d   e   f       # front       back 

# printed: a, b, c, d, e, f

# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

def breadthFirst(root):
  queue = [root]
  # [a]
  while queue:
    curr = queue.pop(0)
    # a, b, c, d, e, f
    print(curr.val)
    # a, b, c
    if curr.left is not None:
      queue.append(curr.left)
      # [b], [c, d],
    if curr.right is not None:
      queue.append(curr.right)
      # [b, c], [c, d, e], [d, e, f]


# breadthFirst(a)


# ex: a b d e c f

#     a
#    / \         
#   b   c      
#  / \   \        #       
# d   e   f       # stack
                  # top  bottom

# printed: a b d e c f

def depthFirst(root):
  stack = [root]
  # [a]
  while stack:
    curr = stack.pop()
    # a, b, d
    print(curr.val)
    # a, b, d
    if curr.right is not None:
      stack.append(curr.right)
      # [c], [c, e], [c, e]
    if curr.left is not None:
      stack.append(curr.left)
      #  [c, b], [c,e,d], [c, e]
    

def depthFirstRecursive(root):
  if not root: return
  print(root.val) 
  depthFirstRecursive(root.left)
  depthFirstRecursive(root.right)



# depthFirstRecursive(a)

# Write a fn that takes in the root of b tree containing numbers as values.
# The fn should return the total sum of values in the tree


#     3
#    / \         
#   5   7      
#  / \   \              
# 1   2   -10   
def sum_tree(root):
  _sum = 0
  stack = [root]
  # [a]
  while stack:
    curr = stack.pop()
    # a, b, d
    _sum += curr.val
    # a, b, d
    if curr.right is not None:
      stack.append(curr.right)
      # [c], [c, e], [c, e]
    if curr.left is not None:
      stack.append(curr.left)
      #  [c, b], [c,e,d], [c, e]
  return _sum
  
def sum_tree_recursive(root):
  if not root: return 0
  return root.val + sum_tree_recursive(root.left) + sum_tree_recursive(root.right)

# a = Node(3)
# b = Node(5)
# c = Node(7)
# d = Node(1)
# e = Node(2)
# f = Node(-10)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# print(sum_tree(a)) # 8
# print(sum_tree_recursive(a)) # 8

# Write depthFirstSearch(root, targetValue)
# return bool whether the target is in the treet

def depthFirstSearch(root, target):
  stack = [root]
  # [a]
  while stack:
    curr = stack.pop()
    # a, b, d
    if curr.val == target: return True
    # a, b, d
    if curr.right is not None:
      stack.append(curr.right)
      # [c], [c, e], [c, e]
    if curr.left is not None:
      stack.append(curr.left)
      #  [c, b], [c,e,d], [c, e]
  return False


def depthFirstSearchRecursive(root, target):
  if not root: return False
  return root.val == target or depthFirstSearchRecursive(root.left, target) or depthFirstSearchRecursive(root.right, target)

# print(depthFirstSearch(a, 2)) # True
# print(depthFirstSearch(a, 100)) # False
# print(depthFirstSearchRecursive(a, 2)) # True
# print(depthFirstSearchRecursive(a, 100)) # False


a = Node(3)
b = Node(5)
c = Node(100)
d = Node(1)
e = Node(2)
f = Node(-10)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
import math
def max_tree(root):
  _max = -math.inf
  stack = [root]
  # [a]
  while stack:
    curr = stack.pop()
    # a, b, d
    if _max < curr.val:
      _max = curr.val
    # a, b, d
    if curr.right is not None:
      stack.append(curr.right)
      # [c], [c, e], [c, e]
    if curr.left is not None:
      stack.append(curr.left)
      #  [c, b], [c,e,d], [c, e]
  return _max
  
def max_tree_recursive(root):
  if not root: return -math.inf
  return max(root.val, max_tree_recursive(root.left), max_tree_recursive(root.right))

print(max_tree_recursive(a)) #  100

