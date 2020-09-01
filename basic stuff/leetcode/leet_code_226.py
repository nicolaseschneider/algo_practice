class Solution(object):
    def invertTree(self, root):
        if not root:
            return root
        temp = root.left
        root.left = root.right
        root.right = temp
        if root.right:
            self.invertTree(root.right)
        if root.left:
            self.invertTree(root.left)
        return root
# cmon now EZ