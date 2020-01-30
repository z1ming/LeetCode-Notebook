class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 初始化哑结点
        dummyhead = cur = ListNode(0)
        # 设置进位
        carry = 0
        p,q = l1,l2
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            sum = x + y + carry 
            carry = sum // 10 # 更新进位的值
            cur.next = ListNode(sum % 10)
            cur = cur.next
            if p: p = p.next
            if q: q = q.next
        if carry == 1:
            end = ListNode(1)
            cur.next = end
        return dummyhead.next