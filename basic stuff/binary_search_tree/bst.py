class BST:
  def  __init__(self, rootNode):
    self.node = rootNode

  def in_order(self, node):
    if (node != None):
      self.in_order(node.left)
      print(node.value)
      self.in_order(node.right)

  def pre_order(self, node):
    if (node != None):
      print(node.value)
      self.pre_order(node.left)
      self.pre_order(node.right)

  def post_order(self, node):
    if (node != None):
      self.post_order(node.left)
      self.post_order(node.right)
      print(node.value)
