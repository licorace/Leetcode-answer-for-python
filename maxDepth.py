#递归法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1 
        
#迭代法
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ 
        stack = []
        if root is not None:
            stack.append((1, root))
        
        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        
        return depth
    
#二叉树的层序建立法
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
    def BuildTree(self,nodeList):
        if nodeList[0] == None:
            return None
        head = TreeNode(nodeList[0])
        Nodes = [head]
        j = 1
        for node in Nodes:
            if node != None:
                node.left = (TreeNode(nodeList[j]) if nodeList[j] != None else None)
                Nodes.append(node.left)
                j += 1
                if j == len(nodeList):
                    return head
                node.right = (TreeNode(nodeList[j]) if nodeList[j] != None else None)
                j += 1
                Nodes.append(node.right)
                if j == len(nodeList):
                    return head
   
