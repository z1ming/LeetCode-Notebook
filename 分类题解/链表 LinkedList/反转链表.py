# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 方法一：迭代
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        res = None
        while head:
            nextnode = head.next
            head.next = res
            res = head
            head = nextnode
        return res
# 时间复杂度：O(n)，假设 n 是列表的长度，时间复杂度是 O(n)。
# 空间复杂度：O(1)。
# 方法二：递归
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        else:
            p = self.reverseList(head.next)
            head.next.next = head
            head.next = None
        return p
# 时间复杂度：O(n)，假设 n 是列表的长度，时间复杂度是 O(n)。
# 空间复杂度：O(n)。最多迭代N次。