# 对链表进行插入排序。
#
#
# 插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
# 每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。
#
#  
#
# 插入排序算法：
#
# 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
# 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
# 重复直到所有输入数据插入完为止。
#  
#
# 示例 1：
#
# 输入: 4->2->1->3
# 输出: 1->2->3->4

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # define a new head, put others after this node
        dummy = ListNode(float('-inf'))
        pre, tail = dummy,dummy
        # 依次将head节点放到dummy后面
        cur = head
        while cur:
            if tail.val < cur.val:
                tail.next = cur
                tail = cur
                cur = cur.next
            else:
                tmp = cur.next
                tail.next = tmp
                while pre.next and pre.next.val < cur.val:
                    pre = pre.next
                # 插入
                cur.next = pre.next
                pre.next = cur
                pre = dummy
                cur = tmp
        return dummy.next