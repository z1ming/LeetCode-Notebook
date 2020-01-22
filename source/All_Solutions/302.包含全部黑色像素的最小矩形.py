# 图片在计算机处理中往往是使用二维矩阵来表示的。

# 假设，这里我们用的是一张黑白的图片，那么 0 代表白色像素，1 代表黑色像素。

# 其中黑色的像素他们相互连接，也就是说，图片中只会有一片连在一块儿的黑色像素（像素点是水平或竖直方向连接的）。

# 那么，给出某一个黑色像素点 (x, y) 的位置，你是否可以找出包含全部黑色像素的最小矩形（与坐标轴对齐）的面积呢？



# 示例:

# 输入:
# [
#   "0010",
#   "0110",
#   "0100"
# ]
# 和 x = 0, y = 2

# 输出: 6

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        l = r = u = d = -1
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == '1':
                    l = j if l == -1 else min(l,j)
                    r = j if r == -1 else max(r,j)
                    u = i if u == -1 else min(u,i)
                    d = i if d == -1 else max(d,i)
        return (d  -u + 1)*(r - l + 1)
