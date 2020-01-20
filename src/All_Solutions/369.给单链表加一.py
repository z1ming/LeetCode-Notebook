# 用一个 非空 单链表来表示一个非负整数，然后将这个整数加一。
#
# 你可以假设这个整数除了 0 本身，没有任何前导的 0。
#
# 这个整数的各个数位按照 高位在链表头部、低位在链表尾部 的顺序排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出: [1,2,4]

class Solution:
    def reverseList(self,head):
        if head is None or head.next is None:
            return head
        tmp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return tmp

    def plusOne(self, head: ListNode) -> ListNode:
        head = self.reverseList(head)
        tmp = head
        head.val += 1
        while (head.val > 9):
            head.val -= 10
            if head.next:
                head.next.val += 1
                head = head.next
            else:
                head.next = ListNode(1)
                break
        return self.reverseList(tmp)