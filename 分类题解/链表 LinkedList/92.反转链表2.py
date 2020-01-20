# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None

        left, right = head,head
        stop = False
        def recurseAndReverse(right,m,n):
            nonlocal left,stop
            if n == 1:
                return

            right = right.next
            if m > 1:
                left = left.next

            recurseAndReverse(right,m - 1,n - 1)
            if left == right or right.next == left:
                stop = True
            if not stop:
                left.val,right.val = right.val,left.val
                left = left.next
        recurseAndReverse(right,m,n)
        return head