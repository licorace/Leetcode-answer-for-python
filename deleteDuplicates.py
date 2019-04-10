# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur =head
        pre=None
        s=set()
        while cur !=None:
            if cur.val not in s:
                s.add(cur.val)      #将当前节点的值存入集合s中
                pre =cur
                cur=cur.next
            else:                   #集合s中含有当前节点的值
                pre.next=cur.next    #跳过当前节点，也可理解为找到重复的节点并删除
                cur=cur.next
           
        return head
