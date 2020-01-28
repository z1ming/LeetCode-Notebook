class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        def count(bound):
            ans = cur = 0
            for x in A :
                cur = cur + 1 if x <= bound else 0
                ans += cur
            return ans

        return count(R) - count(L - 1)

