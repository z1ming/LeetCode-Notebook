# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
# 示例 1:
#
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
# 示例 2:
#
# 输入: 1->1->1->2->3
# 输出: 2->3


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 删除链表一般用双指针加while循环
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        thead = ListNode('a')
        thead.next = head
        pre,cur = None,thead
        while cur:
            pre = cur
            cur = cur.next
            while cur and cur.next and cur.val == cur.next.val:
                t = cur.val
                while cur and cur.val==t:
                    cur = cur.next
                pre.next = cur
        return thead.next