from node import TreeNode
from bst import BST

# 
# Minimal Tree
# given a sorted array with unique integer elements write an algorithm to create a binary search tree with minimal height
#

def solution(nums):
  if not nums:
    return None

  midpoint = len(nums) / 2

  node = TreeNode(nums[midpoint])
  node.left = solution(nums[:midpoint])
  node.right = solution(nums[(midpoint + 1):])
  return node

nums1 = [1,2,3,4,5,6,7,8,9,10]
rootNode = solution(nums1)

# tree = BST(rootNode)
# tree.in_order(rootNode)