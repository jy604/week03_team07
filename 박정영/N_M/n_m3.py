# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# > visited는 중복을 막기 위해서 방문처리를 한 것임으로 visited 없이 재귀를 돌려야함
# 1 1 / 2 2 를 위해서 재귀함수를 n_m(i)로 돌리면 안됨
# 무조건 for문이 1, n+1까지 돌아가도록 설정해줘야함 (n과m1 참고)

n, m = map(int, input().split())
res = []


def n_m():
    # 탈출조건
    if len(res) == m:
        print(' '.join(map(str, res)))
        # 재귀 호출했던 곳으로 돌아가기
        return

    for i in range(1, n+1):
        res.append(i)
        n_m() # 재귀 호출
        res.pop() # 탈출하고 다시 돌아오는 곳

n_m()

