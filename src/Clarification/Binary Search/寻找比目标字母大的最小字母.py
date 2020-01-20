# 给定一个只包含小写字母的有序数组letters 和一个目标字母 target，寻找有序数组里面比目标字母大的最小字母。
#
# 数组里字母的顺序是循环的。举个例子，如果目标字母target = 'z' 并且有序数组为 letters = ['a', 'b']，则答案返回 'a'。
#
# 示例:
#
# 输入:
# letters = ["c", "f", "j"]
# target = "a"
# 输出: "c"
#
# 输入:
# letters = ["c", "f", "j"]
# target = "c"
# 输出: "f"
# 方法一：使用模板2
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lo,hi = 0,len(letters)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if letters[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return letters[lo% len(letters)]
#方法二：调用库
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = bisect.bisect(letters,target)
        return(letters[index % len(letters)])