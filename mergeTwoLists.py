#假设输入是[1,2,4]和[1,3,4],那么节点的变化是l2->l1->l1->l2->l2->l1
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        node = res
        while l1 and l2:
            if l1.val<l2.val:
                node.next,l1 = l1,l1.next #l1这个节点的值赋给node的下一个节点，同时l1将指向下一个节点
            else:
                node.next,l2 = l2,l2.next #l2这个节点的值赋给node的下一个节点，同时l2将指向下一个节点
            node = node.next
        if l1:
            node.next = l1
        else:
            node.next = l2

        result = res.next
        sum = []
        while result is not None:
            sum.append(result.val)
            result = result.next
        print(sum)

if __name__ == '__main__':
    a = eval(input())
    b = eval(input())
    l1 = ListNode(0)
    l2 = ListNode(0)
    cur = l1
    for i in a:
        cur.next = ListNode(i)
        cur = cur.next
    cur = l2
    for i in b:
        cur.next = ListNode(i)
        cur = cur.next
    l1 = l1.next
    l2 = l2.next
    s = Solution()
    s.mergeTwoLists(l1,l2)
