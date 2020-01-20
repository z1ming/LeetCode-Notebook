# 给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。
#
# 示例 1:
#
# 输入: [[0, 30],[5, 10],[15, 20]]
# 输出: 2
# 示例 2:
#
# 输入: [[7,10],[2,4]]
# 输出: 1

# 使用优先队列
# 1. 按照开始时间对会议进行排序
# 2. 初始化一共新的最小堆，将第一个会议的结束时间加入到堆中。我们只需要记录会议的结束时间，告诉我们什么时间房间会空。
# 3. 对每个会议室，检查堆的最小元素是否空闲。
# 4. 处理完所有会议后，堆的大小即为开的房间数量。这就是容纳这些会议需要的孙房间数。
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # if there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0
        # The heap initialization
        free_rooms = []  # 用数组实现堆。。？

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key = lambda x:x[0])

        # Add the first meeting.We have to give a new room to the first meetings.
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for i in intervals[1:]:
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms,i[1])
        return len(free_rooms)