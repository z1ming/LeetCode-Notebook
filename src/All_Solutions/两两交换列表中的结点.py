# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
# 示例:
#
# 给定
# 1->2->3->4, 你应该返回
# 2->1->4->3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 递归的终止条件
        if not (head and head.next):
            return head
        # 假设链表是1->2->3->4,先将结点2保存
        tmp = head.next
        # 递归
        head.next = self.swapPairs(tmp.next)
        # 将1指向剩余结点
        tmp.next = head
        return tmp