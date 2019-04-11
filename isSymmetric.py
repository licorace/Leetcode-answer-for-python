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
#了递归的方法外，我们也可以利用队列进行迭代。队列中每两个连续的结点应该是相等的，而且它们的子树互为镜像。
#最初，队列中包含的是 root 以及 root。该算法的工作原理类似于 BFS，但存在一些关键差异。
#每次提取两个结点并比较它们的值。然后，将两个结点的左右子结点按相反的顺序插入队列中。
#当队列为空时，或者我们检测到树不对称（即从队列中取出两个不相等的连续结点）时，该算法结束。
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = []
        q.append(root)
        q.append(root)
        while len(q) != 0:   #即当队列q为空时退出循环
            t1 = q.pop()
            t2 = q.pop()
            if not t1 and not t2:
                continue
            elif t1 == None or t2 == None:
                return False
            else:
                if t1.val != t2.val:
                    return False
                else:
                    q.append(t1.left)
                    q.append(t2.right)
                    q.append(t1.right)
                    q.append(t2.left)
        return True
            
