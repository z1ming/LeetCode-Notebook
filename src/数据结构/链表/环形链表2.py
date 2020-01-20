# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回
# null。
#
# 为了表示给定链表中的环，我们使用整数
# pos
# 来表示链表尾连接到链表中的位置（索引从
# 0
# 开始）。 如果
# pos
# 是 - 1，则在该链表中没有环。
#
# 说明：不允许修改给定的链表。
#
#
#
# 示例
# 1：
#
# 输入：head = [3, 2, 0, -4], pos = 1
# 输出：tail
# connects
# to
# node
# index
# 1
# 解释：链表中有一个环，其尾部连接到第二个节点。


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 方法一：哈希表
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 使用set保存已经访问过的节点，遍历整个列表，如果返回nul，说明没有环；
        # 如果返回重复元素，说明此时遍历到了环的入口
        visited = set()

        node = head
        while node is not None:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next
        return None