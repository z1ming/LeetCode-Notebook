import bisect
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
        My solution, using sorted list

        Time: O(nlog(k))
        Space: O(n+k)
        """
        res = []
        if not nums or not k:
            return res

        def append_median():
            median = sorted_list[k//2] if k%2==1 else (sorted_list[k//2] + sorted_list[k//2-1])/2
            res.append(median)

        n = len(nums)
        p1, p2 = 0, k
        sorted_list = sorted(nums[p1:p2])
        append_median()

        while p2 != n:
            bisect.insort(sorted_list, nums[p2])
            del_index = bisect.bisect(sorted_list, nums[p1])
            # remember that the index of bisect and list are not same!
            del sorted_list[del_index - 1]
            append_median()
            
            p1 += 1
            p2 += 1

        return res

