# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。
#
# 示例:
#
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        current = 0
        # 将索引入栈
        while current < len(height):
            while stack != [] and height[current] > height[stack[-1]]:
                top = stack[-1]
                stack.pop()
                if not stack:
                    break
                distance = current - stack[-1] - 1
                bounded_height = min(height[current], height[stack[-1]]) - height[top]
                ans += distance * bounded_height

            stack.append(current)
            current += 1
        return ans