# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
#
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
#
# 示例 1:
#
# 输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出: [[1,5],[6,9]]
# 示例 2:
#
# 输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出: [[1,2],[3,10],[12,16]]
# 解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

# 算法：
# 1. 将newInterval之前开始的区间添加到输出
# 2. 添加newInterval到输出，若newInterval与输出中的最后一个区间重合则合并他们
# 3. 一个个添加区间到输出，若有重叠部分则合并他们

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # init data
        new_start, new_end = newInterval
        idx, n = 0, len(intervals)
        output = []

        # add all intervals starting before newInterval
        while idx < n and new_start > intervals[idx][0]:
            output.append(intervals[idx])
            idx += 1

        # add newInterval
        # if there is no overlap,just add the interval
        if not output or output[-1][1] < new_start:
            output.append(newInterval)
        # if there is an overlap,merge with the last interval
        else:
            output[-1][1] = max(output[-1][1], new_end)
        # add next intervals,merge with newInterval if needed
        while idx < n:
            interval = intervals[idx]
            start, end = interval
            idx += 1
            # if there is no overlap,just add an interval
            if output[-1][1] < start:
                output.append(interval)
            # if there is an overlap,merge with the last interval
            else:
                output[-1][1] = max(output[-1][1], end)
        return output
