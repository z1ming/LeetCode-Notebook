# 给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，请你判断一个人是否能够参加这里面的全部会议。
#
# 示例 1:
#
# 输入: [[0,30],[5,10],[15,20]]
# 输出: false
# 示例 2:
#
# 输入: [[7,10],[2,4]]
# 输出: true

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True