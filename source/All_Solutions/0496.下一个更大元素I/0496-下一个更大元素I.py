class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack, hash = [], {}
        for n in nums2:
            while stack and stack[-1] < n:
                hash[stack.pop()] = n
            stack.append(n)
        
        return [hash.get(x, -1) for x in nums1]