""" https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem """


def climbingLeaderboard(ranked, player):
    playerRanks = []
    s = list(set(ranked))
    s.sort(reverse=True)
    i = len(s)
    for score in player:
        while score >= s[i-1] and i>0:
            i -= 1
        playerRanks.append(i+1)
    return playerRanks


if __name__ == '__main__':
    n = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    m = int(input().strip())
    player = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(ranked, player)
    for r in result:
        print(r)