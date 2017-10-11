# 给一组meetings（每个meeting由start和end时间组成）。求出在所有输入meeting时间段内没有会议，也就是空闲的时间段。
# 每个subarray都已经sort好
# 举例：
# [
# [[1, 3], [6, 7]],
# [[2, 4]],
# [[2, 3], [9, 12]]
# ]
# 返回
# [[4, 6], [7, 9]]
import itertools

def meetingRooms(meetings): # merge intervals first, O(nlog(n))
    busyIntervals, flattenMeetings = [], [x for sublist in meetings for x in sublist]
    for meeting in sorted(flattenMeetings, key=lambda m: m[0]):
        if busyIntervals and meeting[0] <= busyIntervals[-1][1]:
            busyIntervals[-1][1] = max(meeting[1], busyIntervals[-1][1])
        else:
            busyIntervals += meeting,
    freeTime = []
    for i, interval in enumerate(busyIntervals):
        if not freeTime and interval[0] > 1:
            freeTime += [1, interval[0]],
        elif i < len(busyIntervals) - 1:
            freeTime += [busyIntervals[i][1], busyIntervals[i+1][0]],
    return freeTime

def meetingRooms1(meetings): # use counter
    flattenTimes, busyCounter, res = [], 0, []
    for meeting in [x for sublist in meetings for x in sublist]:
        flattenTimes += (meeting[0], True),
        flattenTimes += (meeting[1], False),
    flattenTimes.sort(key=lambda i: i[0])
    start = flattenTimes[0][0]
    for time, becomesBusy in flattenTimes:
        if becomesBusy:
            if busyCounter == 0 and time > start:
                res += [start, time],
            busyCounter += 1
        else:
            if busyCounter == 1:
                start = time
            busyCounter -= 1
    return res



meetings =[[[1, 3], [6, 7]],[[2, 4]],[[2, 3], [9, 12]]] 
print(meetingRooms1(meetings))