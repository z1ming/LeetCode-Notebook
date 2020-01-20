# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
# 示例:
#
# 给定的有序链表： [-10, -3, 0, 5, 9],
#
# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMiddle(self,head):
        prevPtr = None
        slowPtr = head
        fastPtr = head
        # 迭代直到快指针到达了链表的结尾
        while fastPtr and fastPtr.next:
            prevPtr = slowPtr
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        # 将链表从慢指针前面断开
        if prevPtr:
            prevPtr.next = None
        return slowPtr

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # 边界情况
        if not head:
            return None
        mid = self.findMiddle(head)
        # 中间的节点变为BST的根节点
        node = TreeNode(mid.val)
        # 如果只有一个链表元素
        if head == mid:
            return node
        # 节点的左子树为递归调用之前的头结点
        node.left = self.sortedListToBST(head)
        # 结点的右子树为递归调用mid.next
        node.right = self.sortedListToBST(mid.next)
        return node