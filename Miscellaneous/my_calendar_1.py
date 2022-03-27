""" https://leetcode.com/problems/my-calendar-i/ """


class MyCalendar:
    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.events:
            if s < end and start < e:
                return False
        self.events.append((start, end))
        return True
