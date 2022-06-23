""" https://leetcode.com/problems/course-schedule-iii/ """

from heapq import *
from typing import *


class Solution:
    # Time: O(n*count); TLE
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda course: course[1])  # sort wrt lastday
        time = count = 0
        for i in range(len(courses)):
            # time + duration <= lastday
            if time + courses[i][0] <= courses[i][1]:
                # add course
                time += courses[i][0]
                courses[count] = courses[i]
                count += 1
            else:
                max_i = i
                # find index of course such that its duration is max
                # of all count number of course durations
                for j in range(count):
                    if courses[j][0] > courses[max_i][0]:
                        max_i = j
                # if max duration > curr duration then replace max
                # duration course with curr course
                if courses[max_i][0] > courses[i][0]:
                    # subtract duration of old course and add new duration
                    time += courses[i][0] - courses[max_i][0]
                    courses[max_i] = courses[i]

        return count

    # Time: O(nlogn); Space: O(n)
    # Same logic as above but optimized using heap
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda course: course[1])  # sort wrt to lastday
        time = 0
        pq = []
        heapify(pq)
        for course in courses:
            if time + course[0] <= course[1]:
                time += course[0]
                heappush(pq, -course[0])
            elif pq:
                max_duration = -nsmallest(1, pq)[0]
                if max_duration > course[0]:
                    time += course[0] - max_duration
                    heapreplace(pq, -course[0])

        return len(pq)
