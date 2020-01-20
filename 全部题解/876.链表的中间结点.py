# 给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
#
# 如果有两个中间结点，则返回第二个中间结点。
#
#  
#
# 示例 1：
#
# 输入：[1,2,3,4,5]
# 输出：此列表中的结点 3 (序列化形式：[3,4,5])
# 返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
# 注意，我们返回了一个 ListNode 类型的对象 ans，这样：
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
# 示例 2：
#
# 输入：[1,2,3,4,5,6]
# 输出：此列表中的结点 4 (序列化形式：[4,5,6])
# 由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head.next == None: # 考虑边界情况
            return head
        if head.next.next == None:
            return head.next
        # 定义保留头节点
        tmp = head
        tmp_list = []
        while tmp:
            tmp_list.append(tmp.val)
            tmp = tmp.next
        for _ in range(len(tmp_list)//2): # 循环结束正好到达中间位置
            head = head.next
        return head
