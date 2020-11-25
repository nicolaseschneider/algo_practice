class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
x = Node('x')
z = Node('z')
y = Node('y')


a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
d.left = x
x.right = z
f.right = y


# Write a fn `levelOrderArray(root)`. The fn should return a 2D where every subarray
# represents the values at a level of the tree.
#     a
#    / \
#   b   c
#  / \   \
# d   e   f
# /       \
# x        y
# \
#  z



# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f'],
# ]


# {
#   node: {
#     val: 'a'
#     left: b
#     right: c
#   },
#   index: 0
# }

def levelOrderArray(root):
  first = {
    "node": root,
    "index": 1,
  }
  resultArray = [];

  queue = [first]

  while queue:
    curr = queue.pop(0)
    # 
    node = curr["node"]
    # b c
    index = curr["index"]
    # 2 2

    if len(resultArray) < index:
      # (0, 1) (1, 2) (2, 2)
      resultArray.append([node.val])
      # [ [a], [ [a], [b] ] ]
    else:
      resultArray[index - 1].append(node.val)
      # [ [a], [b , c]]

    if node.left is not None:
      queue.append({
        "node": node.left,
        "index": index + 1
      })

    if node.right is not None:
      queue.append({
        "node": node.right,
        "index": index + 1
      })

  return resultArray


# print(levelOrderArray(a))

    


# Write a fn called height(root) and returns a number representing the height of the tree.

#   height = 2
#     a
#    / \
#   b   c
#  / \   \
# d   e   f

#   height = 3
#     a
#    / \
#   b   c
#  / \   \
# d   e   f
#     \
#      x

#    height = 4
#     a
#    / \
#   b   c
#  / \   \
# d   e   f
# /       \
# x        y
# \
#  z

# height = 0
#  a


# def height(root):
#   return len(levelOrderArray(root)) - 1


# def height_recursive(root, steps = 0):
#   if not root: return steps - 1
#   return max(height_recursive(root.left, steps + 1), height_recursive(root.right, steps + 1))


# def height_recursive(root):
#   if not root: return -1
#   return max(height_recursive(root.left) + 1, height_recursive(root.right) + 1)




# print(height_recursive(a))


l = [4, 2, 3]

def sum_list(l, sum = 0):
  if not l:
    return sum
  return sum_list(l[1:], sum + l[0])

