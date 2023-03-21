n, m = map(int, input().split())
res = [] # 정답
visited = [0] * (n + 1)


def n_m(start):
    # 탈출조건
    # n과 m이 같을때
    if len(res) == m:
        print(' '.join(map(str, res)))
        return

    for i in range(start, n+1): # 1은 무조건 1부터 시작해서 재귀 돌아와도 1부터 다시 함
        # 이미 방문했으면 건너뛰기
        if visited[i] == 1:
            continue
        visited[i] = 1 # 방문 처리
        res.append(i)
        n_m(i + 1)
        # 다음 자리를 위해 재귀 호출 i+1을 함으로써
        # i = 1일때 다음 n_m()는 무조건 i = 2일때 시작함
        res.pop()
        visited[i] = 0 # 방문 취소


n_m(1)

# input
# 4 2
# output
# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4