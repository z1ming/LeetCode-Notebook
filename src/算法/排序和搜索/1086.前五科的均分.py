# 给你一个不同学生的分数列表，请按 学生的 id 顺序 返回每个学生 最高的五科 成绩的 平均分。
#
# 对于每条 items[i] 记录， items[i][0] 为学生的 id，items[i][1] 为学生的分数。平均分请采用整数除法计算。
#
#  
#
# 示例：
#
# 输入：[[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
# 输出：[[1,87],[2,88]]
# 解释：
# id = 1 的学生平均分为 87。
# id = 2 的学生平均分为 88.6。但由于整数除法的缘故，平均分会被转换为 88。

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        ans = []
        items = sorted(items, key=lambda x: (x[0], x[1]), reverse=True)
        student_id, i = 0, 0
        while i < len(items):
            student_id = items[i][0]
            ave = (items[i][1] + items[i + 1][1] + items[i + 2][1] + items[i + 3][1] + items[i + 4][1]) // 5
            ans.append([student_id, ave])

            while i < len(items):
                if items[i][0] == student_id:
                    i += 1
                else:
                    break

        return ans[::-1]