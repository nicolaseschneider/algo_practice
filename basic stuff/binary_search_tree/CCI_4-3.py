from node import TreeNode
from bst import BST

# given a binary tree design an algorithm which creates a linked list of all the nodes at each depth

def makeBalancedTree(nums):
  if not nums:
    return None

  midpoint = len(nums) / 2

  node = TreeNode(nums[midpoint])
  node.left = solution(nums[:midpoint])
  node.right = solution(nums[(midpoint + 1):])
  return node

def solution(node):
  

nums1 = [1,2,3,4,5,6,7,8,9,10]
rootNode = makeBalancedTree(nums1)