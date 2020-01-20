# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
# 示例 1:
#
# 输入: [3,2,3]
# 输出: 3
#

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = Counter(nums)
        for key,value in dic.items():
            if value > len(nums) / 2:
                return key
# 时间复杂度：O(n).将哈希表迭代一次，哈希表的插入是常数时间的。所以总时间复杂度是O(n)
# 空间复杂度：O(n）哈希表最多包含n-|n/2|个关系，所以占用的空间为O(n)