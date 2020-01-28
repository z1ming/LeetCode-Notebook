class Solution:
    def splitListToParts(self, root, k):
        cur = root 
        l = 0
        res = []
        while cur:
            l += 1
            cur = cur.next
        avg = l //k
        ext = l % k
        for i in range(k):
            res.append(root)
            if root:  #р╙еп╤ооб
                for j in range(1,avg + (i < ext)):
                    root = root.next
                nxt = root.next
                root.next = None
                root = nxt
        return res