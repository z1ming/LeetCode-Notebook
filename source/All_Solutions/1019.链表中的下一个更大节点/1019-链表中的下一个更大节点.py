class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        if not head:
            return []
        nums = []
        cur = head
        while cur:
            nums.append(cur.val)
            cur=cur.next
        stack = [0]
        res = [0]*len(nums)
        for i in range(1,len(nums)):
            while stack and nums[i]>nums[stack[-1]]:
                res[stack[-1]]=nums[i]
                stack.pop()
            stack.append(i)
        return res