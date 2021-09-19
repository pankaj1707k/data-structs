""" https://www.hackerrank.com/challenges/gridland-metro/problem """


def gridlandMetro(n, m, k, track):
    total = n * m
    track_length = 0
    intervals = dict()
    for row in track:
        r, c1, c2 = row
        if r not in intervals:
            intervals[r] = [(c1, c2)]
        else:
            for i in range(len(intervals[r])):
                if c1 <= intervals[r][i][1] and c2 >= intervals[r][i][0]:
                    intervals[r][i] = (
                        min(c1, intervals[r][i][0]),
                        max(c2, intervals[r][i][1]),
                    )
                    break
            else:
                intervals[r].append((c1, c2))

    for l in intervals.values():
        for c1, c2 in l:
            track_length += c2 - c1 + 1

    return total - track_length


if __name__ == "__main__":
    n, m, k = list(map(int, input().rstrip().split()))
    track = []
    for _ in range(k):
        t = list(map(int, input().rstrip().split()))
        track.append(t)
    result = gridlandMetro(n, m, k, track)
    print(result)
