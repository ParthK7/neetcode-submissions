"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        start, end = 0, 0

        for i in range(len(intervals)):
            if intervals[i].start < end:
                return False
            end = max(end, intervals[i].end)
        return True
