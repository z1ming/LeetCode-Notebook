# 不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。
#
# 示例 1:
#
# 输入: a = 1, b = 2
# 输出: 3
# 示例 2:
#
# 输入: a = -2, b = 3
# 输出: 1

# 把大象装进冰箱，需要分三步
# 第一步，打开冰箱门：使用异或获取无进位加法
# 第二步，大象装冰箱：使用与运算获取进位
# 第三步，关上冰箱门：与结果左移一位
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0x100000000
        # 整形最大值
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        while b != 0:
            # 计算进位
            carry = (a & b) << 1
            # 取余范围限制在[0,2^32-1]范围内
            a = (a ^ b) % MASK
            b = carry % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)
