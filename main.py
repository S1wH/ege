TARGET = 41
results = dict()


def gameResult(x):
    if x in results:
        return results[x]
    if x >= TARGET: return 0
    nextCodes = [gameResult(x + 1), gameResult(x + 4), gameResult(x * 3)]
    negative = [c for c in nextCodes if c <= 0]
    if negative:
        res = -max(negative) + 1
    else:
        res = -max(nextCodes)
    results[x] = res
    return res


X = 40
for S in range(X - 1, 0, -1):
    r = gameResult(S)
    print("{:d} {:d}".format(S, r))
