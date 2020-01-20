# 二指输入法定制键盘在 XY 平面上的布局如上图所示，其中每个大写英文字母都位于某个坐标处，例如字母 A 位于坐标 (0,0)，字母 B 位于坐标 (0,1)，字母 P 位于坐标 (2,3) 且字母 Z 位于坐标 (4,1)。
#
# 给你一个待输入字符串 word，请你计算并返回在仅使用两根手指的情况下，键入该字符串需要的最小移动总距离。坐标 (x1,y1) 和 (x2,y2) 之间的距离是 |x1 - x2| + |y1 - y2|。 
#
# 注意，两根手指的起始位置是零代价的，不计入移动总距离。你的两根手指的起始位置也不必从首字母或者前两个字母开始。
#
#  
#
# 示例 1：
#
# 输入：word = "CAKE"
# 输出：3
# 解释：
# 使用两根手指输入 "CAKE" 的最佳方案之一是：
# 手指 1 在字母 'C' 上 -> 移动距离 = 0
# 手指 1 在字母 'A' 上 -> 移动距离 = 从字母 'C' 到字母 'A' 的距离 = 2
# 手指 2 在字母 'K' 上 -> 移动距离 = 0
# 手指 2 在字母 'E' 上 -> 移动距离 = 从字母 'K' 到字母 'E' 的距离  = 1
# 总距离 = 3

class Solution {
public int minimumDistance(String word) {
int len = word.length();
char[] chars = word.toCharArray();
int[][] d = new int[len][len];
int[][] dist = new int[len][len];

for (int i = 0;i < len;i++)
for (int j = i + 1;j < len;j++)
dist[i][j] = distance(chars[i] - 'A', chars[j] - 'A');

for (int i = 1; i < len;i++){
Arrays.fill(d[i], Integer.MAX_VALUE);

for (int j = 0;j < i-1;j++){
// 将原先放在第i-1个字母上的手指移到i上，此时两根手指分别以第i，j-1个字母为终点
d[i][j] = Math.min(d[i][j], d[i-1][j]+dist[i-1][i]);
// 将原先放在第J个字母上的手指移到i上，此时两根手指分别以第i，i-1个字母为终点
d[i][i-1] = Math.min(d[i][i-1], d[i-1][j]+dist[j][i]);
}
d[i][i-1] = Math.min(d[i][i-1], d[i-1][i-1]);
d[i][i] = d[i-1][i-1]+dist[i-1][i];
}
int ret = Integer.MAX_VALUE;
for (int i = 0;i < len-1;i++)
ret = Math.min(ret, d[len-1][i]);


return ret;

}
private
int
distance(int
a, int
b) {
int
x1 = a / 6, y1 = a - 6 * x1;
int
x2 = b / 6, y2 = b - 6 * x2;

return Math.abs(x2 - x1) + Math.abs(y2 - y1);
}
}