# 删除链表中等于给定值 val 的所有节点。
#
# 示例:
#
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5


# 方法一：迭代
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        last = prev.next
        while last:
            if last.val == val:
                prev.next = last.next
                last = prev.next
            else:
                prev = prev.next
                last = last.next
        return dummy.next

# 方法二：递归
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:return
        head.next = self.removeElements(head.next,val)
        return head.next if head.val == val else head