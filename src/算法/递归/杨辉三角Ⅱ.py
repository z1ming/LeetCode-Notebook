# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 3
# 输出: [1,3,3,1]

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # j行的数据是由j-1行的数据计算出来的
        # 假设j-1行为[1,3,3,1]，那么我们在前面插入一个0（j行的数据比j-1行的数据个数多一个）
        # 计算[0+1,1+3,3+3,3+1,1] = [1,4,6,4,1]，最后一个1保留即可
        r = [1]
        for i in range(1, rowIndex + 1):
            r.insert(0, 0)
            for j in range(i):
                r[j] = r[j] + r[j + 1]
        return r
