n, m = map(int, input().split())
res = [] # 정답
visited = [0] * (n + 1)


def n_m():
    # 탈출조건
    # n과 m이 같을때
    if len(res) == m:
        print(' '.join(map(str, res)))
        return

    for i in range(1, n+1):
        # 이미 방문했으면 건너뛰기
        if visited[i] == 1:
            continue
        visited[i] = 1 # 방문 처리
        res.append(i)
        n_m() # 다음 자리를 위해 재귀 호출
        res.pop()
        visited[i] = 0 # 방문 취소


n_m()

# input
# 4 2
# output
# 1 2
# 1 3
# 1 4
# 2 1
# 2 3
# 2 4
# 3 1
# 3 2
# 3 4
# 4 1
# 4 2
# 4 3