""" https://www.hackerrank.com/challenges/minimum-loss/problem """


def minimumLoss(price):
    d = dict()
    n = len(price)
    for i in range(n):
        d[price[i]] = i
    price.sort(reverse=True)
    loss = price[0] - price[-1]
    for i in range(n - 1):
        if d[price[i]] < d[price[i + 1]]:
            loss = min(loss, price[i] - price[i + 1])

    return loss


if __name__ == "__main__":
    n = int(input().strip())
    price = list(map(int, input().rstrip().split()))
    min_loss = minimumLoss(price)
    print(min_loss)
