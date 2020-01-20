# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a,b,p,carry = l1,l2,None,0
        while a or b:
            # 将结点的值相加,如果有进位加上进位
            sum_ = (a.val if a else 0) + (b.val if b else 0) + carry
            # 更新carry和sum的值
            carry,sum_ = sum_ // 10 if sum_ >= 10 else 0,sum_%10
            # 将p结点值赋值给l1
            p,p.val = a if a else b,sum_
            # a,b指针都前进一位
            a,b = a.next if a else None,b.next if b else None
            p.next = a if a else b
        # 考虑边界条件
        if carry:
            p.next = ListNode(carry)
        return l1