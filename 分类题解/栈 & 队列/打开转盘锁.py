# 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转：例如把
# '9'变为'0'，'0'变为'9' 。每次旋转都只能旋转一个拨轮的一位数字。
#
# 锁的初始数字为
# '0000' ，一个代表四个拨轮的数字的字符串。
#
# 列表deadends包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
#
# 字符串target代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 - 1。
#
# 示例1:输入：deadends = ["0201", "0101", "0102", "1212", "2002"], target = "0202"
# 输出：6
# 解释：可能的移动序列为"0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
# 注意
# "0000" -> "0001" -> "0002" -> "0102" -> "0202"这样的序列是不能解锁的，因为当拨动到"0102"时这个锁就会被锁定。
# 示例2:输入: deadends = ["8888"], target = "0009"
# 输出：1
# 解释：
# 把最后一位反向旋转一次即可
# "0000" -> "0009"。
# 示例3:输入: deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], target = "8888"
# 输出：-1
# 解释：
# 无法旋转到目标数字且不被锁定。
# 示例4:输入: deadends = ["0000"], target = "8888"
# 输出：-1
#
# 提示：
# 1.死亡列表deadends的长度范围为[1, 500]。
# 2.目标数字target不会在deadends之中。
# 3.每个deadends和target中的字符串的数字会在10000个可能的情况'0000'到'9999'中产生。
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1,1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i+1:]
        dead = set(deadends)
        queue = collections.deque([('0000',0)])
        seen = {'0000'}
        while queue:
            node,depth = queue.popleft()
            if node == target:return depth
            if node in dead:continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei,depth+1))
        return -1
