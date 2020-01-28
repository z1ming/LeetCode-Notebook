class Solution:
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import Counter,defaultdict
        fre = Counter(nums)
        end = defaultdict(int)
        for num in nums:

            if fre[num] == 0:
                continue
            fre[num] -= 1
            if end[num-1] > 0:
                end[num-1] -= 1
                end[num] += 1
            elif fre[num+1] > 0 and fre[num+2] > 0 :
                fre[num+1] -= 1
                fre[num+2] -= 1
                end[num+2] += 1
            else:
                return False
        return True