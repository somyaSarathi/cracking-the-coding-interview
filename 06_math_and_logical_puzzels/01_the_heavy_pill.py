def heavyPill(pills: list) -> str:
    expectedSum: float = 20*21/2
    sum: float = 0.0

    for i in range(0, 20):
        sum += pills[i]*(i+1)

    if expectedSum == sum:
        return '0'

    ans = '{:.1f}'.format(sum - expectedSum)

    if ans[0] == '0':
        return ans[-1]

    return ans[0]+ans[-1]


if __name__ == '__main__':
    pills = list(map(float, input().split()))
    print(heavyPill(pills))
    exit(0)
