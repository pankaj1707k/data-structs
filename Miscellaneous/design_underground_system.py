""" https://leetcode.com/problems/design-underground-system/ """


class UndergroundSystem:
    def __init__(self):
        # customer_id: [CheckInStation, time]
        self.customer_checkin = {}
        # (start_station, end_station): [total_time, number_of_samples]
        self.total_time = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer_checkin[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        key = (self.customer_checkin[id][0], stationName)
        if key in self.total_time:
            self.total_time[key][0] += t - self.customer_checkin[id][1]
            self.total_time[key][1] += 1
        else:
            self.total_time[key] = [t - self.customer_checkin[id][1], 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        return self.total_time[key][0] / self.total_time[key][1]
