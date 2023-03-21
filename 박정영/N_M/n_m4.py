# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다. > visited 없음
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.


n, m = map(int, input().split())
res = []


def n_m(start):
    if len(res) == m:
        print(' '.join(map(str, res)))
        return

    for i in range(start, n+1):
            res.append(i)
            n_m(i)
            res.pop()

n_m(1)