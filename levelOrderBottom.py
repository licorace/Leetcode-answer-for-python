# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 思路：自上而下，自左向右遍历，最后反转
        if not root:
            return []
        stack = [root]
        output = []
        
        while stack != []:
            temp = []
            for i in range(len(stack)):
                res = stack.pop(0)
                if res is not None:
                    temp.append(res.val)
                    if res.left != None:
                        stack.append(res.left)
                    if res.right != None:
                        stack.append(res.right)
            output.append(temp)
        return output[::-1]
            
        
