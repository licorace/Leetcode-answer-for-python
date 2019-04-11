class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:       #如果p和q都是空树，返回True
            return True
        elif p is not None and q is not None:             #如果p和q都不是空的，继续往下判断
            if p.val == q.val:                            #首节点是相同的
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)  #判断叶节点是否相同
            else:
                return False
        else:                                      #如果p和q其中有一个为空，另一个不为空，则直接返回Fasle
            return False
        
