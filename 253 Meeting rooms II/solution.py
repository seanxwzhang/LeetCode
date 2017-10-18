# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.

class Solution(object):
    def minMeetingRooms(self, intervals): # True for start, False for end
        time_stamps = reduce((lambda x,y: x+y), map(lambda x:[(x.start, True), (x.end, False)], intervals), [])
        sorted_time_stamps = sorted(time_stamps)
        busy_rooms, res = 0, 0
        for time, start_flag in sorted_time_stamps:
            if start_flag:
                busy_rooms += 1
                res = max(res, busy_rooms)
            else:
                busy_rooms -= 1
        return res

s = Solution()
print(s.minMeetingRooms([[2,7]]))