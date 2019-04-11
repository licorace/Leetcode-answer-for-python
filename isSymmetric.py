#递归方法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root,root)
    def isMirror(self,t1,t2):
        if not t1 and not t2:
            return True
        elif t1 != None and t2 != None:
            if t1.val == t2.val:
                return self.isMirror(t1.right,t2.left) and self.isMirror(t1.left,t2.right)
            else:   
                return False
        else:
            return False
          
#迭代法
