# 给定一位研究者论文被引用次数的数组（被引用次数是非负整数），数组已经按照升序排列。编写一个方法，计算出研究者的 h 指数。
#
# h 指数的定义: “h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）至多有 h 篇论文分别被引用了至少 h 次。（其余的 N - h 篇论文每篇被引用次数不多于 h 次。）"
#
#  
#
# 示例:
#
# 输入: citations = [0,1,3,5,6]
# 输出: 3
# 解释: 给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 0, 1, 3, 5, 6 次。
#      由于研究者有 3 篇论文每篇至少被引用了 3 次，其余两篇论文每篇被引用不多于 3 次，所以她的 h 指数是 3。

class Solution {
    public int hIndex(int[] citations) {
        int len = citations.length;
        if (len == 0 || citations[len-1] == 0){
            return 0;
        }
        int left = 0;
        int right = len - 1;
        while (left < right){
            int mid = (left + right)>>>1;
            // 比长度小，就得去掉该值
            if (citations[mid]<len-mid){
                left = mid + 1;
            }else{
                // 比长度大的事满足的，我们应该继续让mid向左走尝试看有没有更小的mid值
                // 可以满足mid对应的值大于等于从[mid,len-1]的长度
                right=mid;

            }
        }
        return len - left;
    }
}